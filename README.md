URL based webpage classification on Dmoz dataset
================================================

We have used two scripts process.sh and testprocess.sh. process.sh is used for the training dataset and testprocess.sh is used for the testing dataset.
process.sh and testprocess.sh executes the following program:

1) preprocess.py
* it preprocesses each URL

2) 3ngrams.py
* this file finds the tokens, 3 grams, 4 grams and 5 grams

3) uniqueW.py
* find the unique words

4) CreateVec.py
* finds the term frequency

5) featureweighing.py
* finds the value of weighting methods such as idf, pidf, dsidf, mi, chi and ig

6) multiplyCOL.py
* finds variants of tf such as tf.idf, tf.pidf, tf.dsidf, tf.mi, tf.chi and tf.ig

7) finalVec.py
* produces the file in the format supported by SVM_LIGHT.

The final output from finalVec.py is then fed to "SVM_LIGHT" inorder to find the accuracy, precision and recall.
