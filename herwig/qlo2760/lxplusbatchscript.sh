#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpt0_15
bsub -R "pool>5000" -M 3000000 -q 1nd -J job1C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpt0_15/submit_LO_2760_0_15.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat15_30
bsub -R "pool>5000" -M 3000000 -q 1nd -J job2C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat15_30/submit_LO_2760_15_30.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat30_50
bsub -R "pool>5000" -M 3000000 -q 1nd -J job3C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat30_50/submit_LO_2760_30_50.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat50_80
bsub -R "pool>5000" -M 3000000 -q 1nd -J job4C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat50_80/submit_LO_2760_50_80.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat80_120
bsub -R "pool>5000" -M 3000000 -q 1nd -J job5C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat80_120/submit_LO_2760_80_120.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat120_170
bsub -R "pool>5000" -M 3000000 -q 1nd -J job6C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat120_170/submit_LO_2760_120_170.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat170_220
bsub -R "pool>5000" -M 3000000 -q 1nd -J job7C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat170_220/submit_LO_2760_170_220.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat220_280
bsub -R "pool>5000" -M 3000000 -q 1nd -J job8C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat220_280/submit_LO_2760_220_280.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat280_370
bsub -R "pool>5000" -M 3000000 -q 1nd -J job9C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat280_370/submit_LO_2760_280_370.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat370_460
bsub -R "pool>5000" -M 3000000 -q 1nd -J job10C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat370_460/submit_LO_2760_370_460.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat460_540
bsub -R "pool>5000" -M 3000000 -q 1nd -J job11C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat460_540/submit_LO_2760_460_540.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat540_5000
bsub -R "pool>5000" -M 3000000 -q 1nd -J job12C < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qlo2760/dirpthat540_5000/submit_LO_2760_540_5000.sh


echo "submitted all jobs!"

