python preprocess.py ../tf.idf/train/middle1.csv ../tf.idf/train/middle11.csv
python preprocess.py ../tf.idf/train/middle2.csv ../tf.idf/train/middle22.csv
python 3ngrams.py ../tf.idf/train/middle11.csv ../tf.idf/train/middle111.csv
python 3ngrams.py ../tf.idf/train/middle22.csv ../tf.idf/train/middle222.csv
#cat ../ouput1/*.txt >>../ouput1/middle
#cat ../output2/*.txt >>../output2/middle2

cat ../tf.idf/train/middle111.csv ../tf.idf/train/middle222.csv > ../tf.idf/train/uniq_wo.txt

python uniqueW.py ../tf.idf/train/uniq_wo.txt ../tf.idf/train/unique_wordlist.txt
#sed 's/ \+/,/g' ../output12/unique_wordlist.txt > ../output12/unique_wordlist.csv
python CreateVec.py ../tf.idf/train/middle111.csv ../tf.idf/train/unique_wordlist.txt ../tf.idf/train/train1.csv
python CreateVec.py ../tf.idf/train/middle222.csv ../tf.idf/train/unique_wordlist.txt ../tf.idf/train/train2.csv
#sed 's/ \+/,/g' ../ouput1/middle > ../ouput1/middle.csv
#sed 's/ \+/,/g' ../output2/middle2 > ../output2/middle2.csv'''
python featureweighing.py ../tf.idf/train/middle111.csv ../tf.idf/train/middle222.csv ../tf.idf/train/featureweighingtraining.csv ../tf.idf/train/unique_wordlist.txt 

cat ../tf.idf/train/train1.csv ../tf.idf/train/train2.csv > ../tf.idf/train/train.csv
python multiplyCOL.py ../tf.idf/train/idf.csv ../tf.idf/train/featureweighingtraining.csv ../tf.idf/train/train.csv ../tf.idf/train/idf1.csv

for i in $(seq 33220)
do
  echo 1
done > ../tf.idf/train/t1

for i in $(seq 33220)
do
  echo -1
done > ../tf.idf/train/t2

cat ../tf.idf/train/t1 ../tf.idf/train/t2 > ../tf.idf/train/groundfile.csv

python finalVec.py ../tf.idf/train/groundfile.csv ../tf.idf/train/idf.csv ../tf.idf/train/training.dat
