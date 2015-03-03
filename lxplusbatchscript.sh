#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript


bsub -R "pool>5000" -M 3000000 -q 1nd -J job1 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job2 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job3 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job4 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job5 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job6 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job7 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job8 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job9 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job10 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job11 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job12 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020/submit_LO_5020_540_5000.sh


bsub -R "pool>5000" -M 3000000 -q 1nd -J job13 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job14 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job15 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job16 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job17 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job18 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job19 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job20 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job21 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job22 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job23 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job24 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/had5020/submit_HAD_5020_540_5000.sh

echo "submitted all jobs!"

