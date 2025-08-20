import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



genes_tissues = sys.argv[1:-1]
out_file = sys.argv[-1]

genes = genes_tissues[:-1:2]
tissues = genes_tissues[1::2]

counts = []
for i in range(len(genes)):

    gene = genes[i]
    tissue = tissues[i]

    sample_to_count_map = {}

    f = open(gene + '_counts.txt')
    for l in f:
        A = l.rstrip().split()
        sample_to_count_map[A[0]] = int(A[1])

    f.close()

    count = []

    f = open(tissue + '_samples.txt')
    for l in f:
        sample = l.rstrip()
        if sample in sample_to_count_map:
            count.append(sample_to_count_map[sample])
    f.close()

    counts.append(count)



width=len(genes) * 3
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

for i in range(len(genes)):
    ax = fig.add_subplot(1,len(counts),1+i)
    ax.hist(counts[i])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(genes[i] + ' ' + tissues[i])

plt.savefig(out_file,bbox_inches='tight')
