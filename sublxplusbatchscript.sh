#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript


bsub -R "pool>5000" -M 3000000 -q 1nd -J job25 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job26 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job27 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job28 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job29 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job30 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job31 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job32 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job33 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job34 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job35 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job36 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/relo7000/submit_LO_7000_540_5000.sh


bsub -R "pool>5000" -M 3000000 -q 1nd -J job37 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job38 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job39 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job40 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job41 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job42 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job43 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job44 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job45 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job46 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job47 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job48 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000/submit_HAD_7000_540_5000.sh

echo "submitted all jobs!"

