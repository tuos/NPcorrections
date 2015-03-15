#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpt0_15
bsub -R "pool>5000" -M 3000000 -q 1nd -J job1 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpt0_15/submit_HAD_7000_0_15.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat15_30
bsub -R "pool>5000" -M 3000000 -q 1nd -J job2 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat15_30/submit_HAD_7000_15_30.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat30_50
bsub -R "pool>5000" -M 3000000 -q 1nd -J job3 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat30_50/submit_HAD_7000_30_50.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat50_80
bsub -R "pool>5000" -M 3000000 -q 1nd -J job4 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat50_80/submit_HAD_7000_50_80.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat80_120
bsub -R "pool>5000" -M 3000000 -q 1nd -J job5 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat80_120/submit_HAD_7000_80_120.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat120_170
bsub -R "pool>5000" -M 3000000 -q 1nd -J job6 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat120_170/submit_HAD_7000_120_170.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat170_220
bsub -R "pool>5000" -M 3000000 -q 1nd -J job7 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat170_220/submit_HAD_7000_170_220.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat220_280
bsub -R "pool>5000" -M 3000000 -q 1nd -J job8 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat220_280/submit_HAD_7000_220_280.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat280_370
bsub -R "pool>5000" -M 3000000 -q 1nd -J job9 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat280_370/submit_HAD_7000_280_370.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat370_460
bsub -R "pool>5000" -M 3000000 -q 1nd -J job10 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat370_460/submit_HAD_7000_370_460.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat460_540
bsub -R "pool>5000" -M 3000000 -q 1nd -J job11 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat460_540/submit_HAD_7000_460_540.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat540_5000
bsub -R "pool>5000" -M 3000000 -q 1nd -J job12 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/rehad7000/dirpthat540_5000/submit_HAD_7000_540_5000.sh


echo "submitted all jobs!"

