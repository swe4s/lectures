import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



gene_tissue_pairs = sys.argv[1:]

counts = []
titles = []

for gene_tissue_pair in gene_tissue_pairs:
    gene = gene_tissue_pair.split(',')[0]
    tissue = gene_tissue_pair.split(',')[1]

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
    titles.append(gene_tissue_pair)


out_file = '_'.join(gene_tissue_pairs) + '.png'

width=len(counts) * 3
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

for i in range(len(counts)):
    ax = fig.add_subplot(1,len(counts),1+i)
    ax.hist(counts[i])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(gene_tissue_pairs[i])

plt.savefig(out_file,bbox_inches='tight')
