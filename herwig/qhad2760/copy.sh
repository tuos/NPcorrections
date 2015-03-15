#!/bin/sh

rm -rf dirpthat*

mkdir dirpthat15_30
cd dirpthat15_30
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
cd ..

mkdir dirpthat30_50
cd dirpthat30_50
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/50/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/30/g' <tmp.sh >submit_HAD_2760_30_50.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat50_80
cd dirpthat50_80
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/80/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/50/g' <tmp.sh >submit_HAD_2760_50_80.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat80_120
cd dirpthat80_120
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/120/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/80/g' <tmp.sh >submit_HAD_2760_80_120.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat120_170
cd dirpthat120_170
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/170/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/120/g' <tmp.sh >submit_HAD_2760_120_170.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat170_220
cd dirpthat170_220
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/220/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/170/g' <tmp.sh >submit_HAD_2760_170_220.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat220_280
cd dirpthat220_280
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/280/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/220/g' <tmp.sh >submit_HAD_2760_220_280.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat280_370
cd dirpthat280_370
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/370/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/280/g' <tmp.sh >submit_HAD_2760_280_370.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat370_460
cd dirpthat370_460
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/460/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/370/g' <tmp.sh >submit_HAD_2760_370_460.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat460_540
cd dirpthat460_540
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/540/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/460/g' <tmp.sh >submit_HAD_2760_460_540.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..

mkdir dirpthat540_5000
cd dirpthat540_5000
cp ../customiseGEN2_cfi.py .
cp ../anaGenJet_HAD_Herwig_cfg.py .
cp ../submit_HAD_2760_15_30.sh .
sed 's/30/5000/g' <submit_HAD_2760_15_30.sh >tmp.sh
sed 's/15/540/g' <tmp.sh >submit_HAD_2760_540_5000.sh
rm tmp.sh
rm submit_HAD_2760_15_30.sh
cd ..



