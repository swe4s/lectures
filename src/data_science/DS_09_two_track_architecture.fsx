
open System
open System.Web
open System.IO
open Newtonsoft.Json
open System.Configuration
open System.Data.SqlClient
open System.Collections.ObjectModel
open System.Linq
open System.Net
open System.Data
open System.Net.Mail

type Product = {Id: int; Sku: string}
type OrderLineItem = {Id:int; BilledAmount: float; Discount: float; Tax: float; Product: Product}
type Order = {Id: int; OpenedDate: DateTime; ClosedDate: DateTime; LineItems: OrderLineItem seq}
type Customer = {Id: int; FirstName: string; LastName: string; EMail: string; Order: Order; IsPreferred: Boolean}

type FailureType =
    | BadPayload
    | InvalidCustomerName
    | CustomerNotInSystem
    | CustomerDatabaseDown
    | OrderItemsNotInStock
    | OrderSystemDown
    | AttachmentPointNotSetInConfiguration
    | SendAcknoeledgementEmailFailed
    | SendToFullfillmenetFailed
    | SendFullfillmentEmailFailed

type ActionResult<'T> =
    | Success of 'T
    | Failure of FailureType

let bind someFunction input =
    match input with 
    | Success t -> someFunction t
    | Failure f -> Failure f

let (>>=) input someFunction = 
    bind someFunction input

let validateCustomer customer =
    let invalidFirstName = String.IsNullOrEmpty(customer.FirstName)
    let invalidLastName = String.IsNullOrEmpty(customer.LastName)
    match invalidFirstName, invalidFirstName with
    | false, false -> Success customer
    | _, _ -> Failure InvalidCustomerName

let systemCheckCustomer customer =
    try
        let connectionString = ConfigurationManager.ConnectionStrings.["database"].ConnectionString
        use connection = new SqlConnection(connectionString)
        let commandText = "usp_verifyInvoince"
        use command = new SqlCommand(commandText)
        command.CommandType <- CommandType.StoredProcedure
        command.Parameters.Add(customer.Id) |> ignore
        connection.Open()
        let isInSystem = command.ExecuteScalar() :?> Boolean
        match isInSystem with
        | true -> Success customer
        | false -> Failure CustomerNotInSystem
    with _ -> Failure CustomerDatabaseDown

let systemCheckOrderItems customer =
    try
        use client = new WebClient()
        let uri = ConfigurationManager.AppSettings.["WarehouseUri"];
        let isAnyOutOfStock =
            customer.Order.LineItems
            |> Seq.map(fun li -> client.DownloadString(uri + li.Id.ToString()))
            |> Seq.map(fun r -> JsonConvert.DeserializeObject<Boolean>(r))
            |> Seq.contains(false)
        match isAnyOutOfStock with
        | true -> Failure OrderItemsNotInStock
        | false -> Success customer
    with _ -> Failure OrderSystemDown

let applyOrderDiscount customer =
    try
        let attachmentPoint = float.Parse(ConfigurationManager.AppSettings.["AttachmentPoint"])
        let totalBill = customer.Order.LineItems |> Seq.sumBy(fun i -> i.BilledAmount + i.Tax)
        match totalBill > attachmentPoint, customer.IsPreferred with
        | true, true ->
            let newLineItems = customer.Order.LineItems |> Seq.map(fun li -> {li with Discount = li.Discount * 0.95})
            let newOrder = {customer.Order with LineItems = newLineItems}
            let newCustomer = {customer with Order = newOrder}
            Success newCustomer
        | _, _ -> Success customer
    with _ -> Failure AttachmentPointNotSetInConfiguration

let sendEmailConfirmation customer =
    try
        let emailTo = customer.EMail
        let from = ConfigurationManager.AppSettings.["fromAddress"]
        let subject = String.Format("Your Order {0} From This Awesome Company Has Been Received", customer.Order.Id)
        let body = "We'll let you know when the items have shipped"
        use client = new SmtpClient()
        client.Send(from, emailTo, subject, body)
        Success customer
    with _ -> Failure SendAcknoeledgementEmailFailed

let sendToFullfillmentWarehouse customer =
    try
        use client = new WebClient()
        let uri = ConfigurationManager.AppSettings.["FullFillmentUri"]
        let json = JsonConvert.SerializeObject(customer)
        let response = client.UploadString(uri, json)
        Success customer
    with _ -> Failure SendToFullfillmenetFailed

let handleFullfillmentStaus customer =
    try
        let emailTo = customer.EMail
        let from = ConfigurationManager.AppSettings.["fromAddress"]
        let subject = String.Format("Your Order {0} From This Awesome Company Has Been Shipped", customer.Order.Id)
        let body = "Something bad happened"
        use client = new SmtpClient()
        client.Send(from, emailTo, subject, body)
        Success customer
    with _ -> Failure SendAcknoeledgementEmailFailed

let getCustomer (request: HttpRequest) =
    use stream = request.InputStream
    use reader = new StreamReader(stream)
    let contents = reader.ReadToEnd()
    match String.IsNullOrEmpty(contents) with
    | true -> Failure BadPayload
    | false -> Success (JsonConvert.DeserializeObject<Customer>(contents))

let handleRequest (request: HttpRequest) =
    let customer = getCustomer request
    customer
    >>= validateCustomer
    >>= systemCheckCustomer
    >>= systemCheckOrderItems
    >>= applyOrderDiscount
    >>= sendEmailConfirmation
    >>= sendToFullfillmentWarehouse
    >>= handleFullfillmentStaus

let writeFailure failure =
    //Logger.Write(failure.ToString())
    ()

[<EntryPoint>]
let main argv =
    Console.WriteLine("Starting")
    while true do
        let request = new HttpRequest("","","")
        match (handleRequest request) with
        | Success c -> ()
        | Failure f -> writeFailure(f)
    0