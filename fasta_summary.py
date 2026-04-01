import sys

#Input file
Input=sys.argv[1]

sequence={}
seq_id=""
seq=""

with open(Input,"r")as f:
        for line in f:
                line=line.strip()
                if line.startswith(">"):
                        if seq_id:
                                sequence[seq_id]=seq
                        seq_id=line[1:]
                        seq=""
                else:
                        seq += line.upper()
        if seq_id:
                sequence[seq_id]=seq

#variables
total_gc=0
total_len=0
longest_id=""
shortes_id=""
max_len=0
min_len=float("inf")
details=[]
# formulation
for id, sequence in sequence.items():
        length=len(sequence)
        gc_count=sequence.count("G") +sequence.count("C")
        gc_percent=(gc_count/length)*100 if length>0 else 0
        details.append(f"{id}\t{length}\t{round(gc_percent,2)}")
        total_gc +=gc_percent
        total_len +=length

#to find longest seq
        if length> max_len:
                max_len=length
                longest_id=id
#to shortest seq
        if length<min_len:
                min_len=length
                shortes_id=id

#Average GC%
avg_GC=(total_gc/ len(sequence)) if len(sequence)>0 else 0

#save summary
with open("summary.txt","w") as out:
        out.write("FASTA SUMMARY REPORT\n")
        out.write("---------------------\n")
        out.write(f"Total sequences: {len(sequence)}\n")
        out.write(f"Average GC%: {round(avg_GC,2)}\n")
        out.write(f"Longest Sequence : {longest_id} ({max_len} bp)\n")
        out.write(f"Shortest Sequence : {shortes_id} ({min_len} bp)\n")
  #this is for per base count with store in details variable
        out.write("\nper sequence states: \n")
        out.write("ID\tlength\tgc%\n")
        for line in details:
                out.write(line+"\n")
print("Summary report is ready")
