#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpt0_15
bsub -R "pool>5000" -M 3000000 -q 1nd -J job1A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpt0_15/submit_LO_5020_0_15.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat15_30
bsub -R "pool>5000" -M 3000000 -q 1nd -J job2A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat15_30/submit_LO_5020_15_30.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat30_50
bsub -R "pool>5000" -M 3000000 -q 1nd -J job3A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat30_50/submit_LO_5020_30_50.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat50_80
bsub -R "pool>5000" -M 3000000 -q 1nd -J job4A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat50_80/submit_LO_5020_50_80.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat80_120
bsub -R "pool>5000" -M 3000000 -q 1nd -J job5A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat80_120/submit_LO_5020_80_120.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat120_170
bsub -R "pool>5000" -M 3000000 -q 1nd -J job6A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat120_170/submit_LO_5020_120_170.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat170_220
bsub -R "pool>5000" -M 3000000 -q 1nd -J job7A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat170_220/submit_LO_5020_170_220.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat220_280
bsub -R "pool>5000" -M 3000000 -q 1nd -J job8A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat220_280/submit_LO_5020_220_280.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat280_370
bsub -R "pool>5000" -M 3000000 -q 1nd -J job9A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat280_370/submit_LO_5020_280_370.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat370_460
bsub -R "pool>5000" -M 3000000 -q 1nd -J job10A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat370_460/submit_LO_5020_370_460.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat460_540
bsub -R "pool>5000" -M 3000000 -q 1nd -J job11A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat460_540/submit_LO_5020_460_540.sh

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat540_5000
bsub -R "pool>5000" -M 3000000 -q 1nd -J job12A < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/lo5020/dirpthat540_5000/submit_LO_5020_540_5000.sh


echo "submitted all jobs!"

