#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript


bsub -R "pool>5000" -M 3000000 -q 1nd -J job49 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job50 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job51 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job52 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job53 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job54 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job55 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job56 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job57 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job58 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job59 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job60 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760/submit_LO_2760_540_5000.sh


bsub -R "pool>5000" -M 3000000 -q 1nd -J job61 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_0_15.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job62 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_15_30.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job63 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_30_50.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job64 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_50_80.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job65 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_80_120.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job66 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_120_170.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job67 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_170_220.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job68 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_220_280.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job69 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_280_370.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job70 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_370_460.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job71 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_460_540.sh
bsub -R "pool>5000" -M 3000000 -q 1nd -J job72 < /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760/submit_HAD_2760_540_5000.sh

echo "submitted all jobs!"

