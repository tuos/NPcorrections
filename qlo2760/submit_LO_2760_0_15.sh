cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760

cmsRun anaGenJet_LO_cfg.py output="GenJet_LO_R23457_2760_Mar2_Z2pt0to15.root" maxEvents="1000000" processType="NSD" ptHatLow="0" ptHatHigh="15" sqrtS="2760" &> run_LO_2760_0_15.log
