# clean up trace results
rm *.txt
rm *.csv
echo "generating trace"

python3 mem2page.py
echo " mem to page done"
python3 filter_pmap.py
echo " filter pmap done"
python3 page2delta.py
echo " page to delta done"
python3 deltaFilter.py
echo " delta filter done"
# python3 delta2onehot.py
# echo " delta to onehot done"
# python3 modelGen.py
python3 gencsv.py filted_delta.txt traces.csv
echo "done"
