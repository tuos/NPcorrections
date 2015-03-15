cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qlo2760

cmsRun anaGenJet_LO_cfg.py output="GenJet_LO_R23457_2760_Mar2_Z2pt30to50.root" maxEvents="1000000" processType="NSD" ptHatLow="30" ptHatHigh="50" sqrtS="2760" &> run_LO_2760_30_50.log
