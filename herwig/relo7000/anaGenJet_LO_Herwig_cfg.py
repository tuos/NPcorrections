import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import os

process = cms.Process('GEN')

# var parsing # 
options = VarParsing.VarParsing ('standard')
options.maxEvents = 10
#options.qLimit         = 20000

options.register('qLimit',
                 20000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Q2 Limit")

options.register('ptHatLow',
                 15,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Minimum pt-hat")

options.register('ptHatHigh',
                 1000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum pt-hat")

processType = 'NSD'

otFile = 'GenJet_LO_R23475_2760_Herwig_analyzer_%d_qLimit_%d_pthat_%d_20140910.root' % (options.qLimit,options.ptHatLow,options.ptHatHigh)

ptmin          = str(options.ptHatLow)
ptmax          = str(options.ptHatHigh)

options.parseArguments()

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic2p76TeV2013Collision_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# Input source
process.source = cms.Source("EmptySource")

#from JetAnalyzer.JetAnalyzer.readpythiaevents_cfi import *
#readpythiaevents.srcGenJets    = cms.InputTag('ak7GenJets::GEN')
#readpythiaevents.q_binLimit    = cms.double(qLimit)
#process.readpythiaevents = readpythiaevents
#process.rdpy = cms.EndPath(process.readpythiaevents)

###output TFile--------------------------------- 
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(otFile),
    #closeFileFast = cms.untracked.bool(True)
)


# Output definition

#process.output = cms.OutputModule("PoolOutputModule",
                                  
#                                  splitLevel = cms.untracked.int32(0),
#                                  outputCommands = cms.untracked.vstring('drop *'),
                                  
#                                  fileName = cms.untracked.string('EDMOutput.root'),
                                  
#                                  dataset = cms.untracked.PSet(
#                                      dataTier = cms.untracked.string(''),
#                                      filterName = cms.untracked.string('')
#                                  ),
#                                  SelectEvents = cms.untracked.PSet(
#                                      SelectEvents = cms.vstring('generation_step')
#                                  )
#)


# Other statements
process.GlobalTag.globaltag = 'STARTHI53_V28::All'

herwigDefaultsBlock = cms.PSet(
    dataLocation = cms.string('/cvmfs/cms.cern.ch/slc5_amd64_gcc462/external/herwigpp/2.5.0-cms7/share/Herwig++'),
    
    repository = cms.string('HerwigDefaults.rpo'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    
    run = cms.string('LHC'),
    
    cmsDefaults = cms.vstring(
        '+pdfMRST2001',
        '+cm2p76TeV',
        '+ue_2_3',
        '+basicSetup',
        '+setParticlesStableForDetector',
    ),
    
    basicSetup = cms.vstring(
        'cd /Herwig/Generators',
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue',
        'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue',
        'set LHCGenerator:NumberOfEvents 10000000',
        'set LHCGenerator:DebugLevel 0', #1
        'set LHCGenerator:PrintEvent 0', #0
        'set LHCGenerator:MaxErrors  10000', #10000
        'cd /Herwig/Particles',
        'set p+:PDF /Herwig/Partons/cmsPDFSet',
        'set pbar-:PDF /Herwig/Partons/cmsPDFSet',
        'set K0:Width 1e300*GeV',
        'set Kbar0:Width 1e300*GeV',
        'cd /',
    ),
    
    # PDF presets
    ##############################
    
    # Default pdf for Herwig++ 2.3
    pdfMRST2001 = cms.vstring(
        'cd /Herwig/Partons',
        'create Herwig::MRST MRST2001 HwMRST.so',
        'setup MRST2001 ${HERWIGPATH}/PDF/mrst/2001/lo2002.dat',
        'set MRST2001:RemnantHandler HadronRemnants',
        'cp MRST2001 cmsPDFSet',
        'cd /',
    ),
    # Default pdf for Herwig++ 2.4
    pdfMRST2008LOss = cms.vstring(
        'cp /Herwig/Partons/MRST /Herwig/Partons/cmsPDFSet',
    ),
    pdfCTEQ5L = cms.vstring(
        'cd /Herwig/Partons',
        'create ThePEG::LHAPDF CTEQ5L ThePEGLHAPDF.so',
        'set CTEQ5L:PDFName cteq5l.LHgrid',
        'set CTEQ5L:RemnantHandler HadronRemnants',
        'cp CTEQ5L cmsPDFSet',
        'cd /',
    ),
    pdfCTEQ6L1 = cms.vstring(
        'cd /Herwig/Partons',
        'create ThePEG::LHAPDF CTEQ6L1 ThePEGLHAPDF.so',
        'set CTEQ6L1:PDFName cteq6ll.LHpdf',
        'set CTEQ6L1:RemnantHandler HadronRemnants',
        'cp CTEQ6L1 cmsPDFSet',
        'cd /',
    ),
    
    # CME presets
    ##############################
    cm2p76TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 2760.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV',
    ),
    cm5p02TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 5020.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV',
    ),
    cm7TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV',
    ),
    cm8TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 8000.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV',
    ),
    cm10TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV',
    ),
    cm14TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV',
    ),
    
    # UE tunes
    ##############################
    
    # UE Tune from Herwig++ 2.3 (MRST2001)
    ue_2_3 = cms.vstring(
        'cd /Herwig/UnderlyingEvent',
        'set KtCut:MinKT 4.0',
        'set UECuts:MHatMin 8.0',
        'set MPIHandler:InvRadius 1.5',
        'cd /',
    ),
    # UE Tune from Herwig++ 2.4 (MRST2008LO**)
    ue_2_4 = cms.vstring(
        'cd /Herwig/UnderlyingEvent',
        'set KtCut:MinKT 4.3',
        'set UECuts:MHatMin 8.6',
        'set MPIHandler:InvRadius 1.2',
        'cd /',
    ),
    
    # reweight presets
    ##############################
    
    reweightConstant = cms.vstring(
        'mkdir /Herwig/Weights',
        'cd /Herwig/Weights',
        'create ThePEG::ReweightConstant reweightConstant ReweightConstant.so',
        'cd /',
        'set /Herwig/Weights/reweightConstant:C 1',
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightConstant',
    ),
    reweightPthat = cms.vstring(
        'mkdir /Herwig/Weights',
        'cd /Herwig/Weights',
        'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so',
        'cd /',
        'set /Herwig/Weights/reweightMinPT:Power 4.5',
        'set /Herwig/Weights/reweightMinPT:Scale 15*GeV',
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightMinPT',
    ),
    
    # Disable decays of particles with ctau > 10mm
    setParticlesStableForDetector = cms.vstring(
        'cd /Herwig/Particles',
        'set mu-:Stable Stable',
        'set mu+:Stable Stable',
        'set Sigma-:Stable Stable',
        'set Sigmabar+:Stable Stable',
        'set Lambda0:Stable Stable',
        'set Lambdabar0:Stable Stable',
        'set Sigma+:Stable Stable',
        'set Sigmabar-:Stable Stable',
        'set Xi-:Stable Stable',
        'set Xibar+:Stable Stable',
        'set Xi0:Stable Stable',
        'set Xibar0:Stable Stable',
        'set Omega-:Stable Stable',
        'set Omegabar+:Stable Stable',
        'set pi+:Stable Stable',
        'set pi-:Stable Stable',
        'set K+:Stable Stable',
        'set K-:Stable Stable',
        'set K_S0:Stable Stable',
        'set K_L0:Stable Stable',
        'cd /',
    ),
    
    # Default settings for using LHE files
    lheDefaults = cms.vstring(
        'cd /Herwig/Cuts',
        'create ThePEG::Cuts NoCuts',
        'cd /Herwig/EventHandlers',
        'create ThePEG::LesHouchesInterface LHEReader',
        'set LHEReader:Cuts /Herwig/Cuts/NoCuts',
        'create ThePEG::LesHouchesEventHandler LHEHandler',
        'set LHEHandler:WeightOption VarWeight',
        'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor',
        'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler',
        'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler',
        'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler',
        'insert LHEHandler:LesHouchesReaders 0 LHEReader',
        'cd /Herwig/Generators',
        'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler',
        'cd /Herwig/Shower',
        'set Evolver:HardVetoScaleSource Read',
        'set Evolver:MECorrMode No',
        'cd /',
    ),
    lheDefaultPDFs = cms.vstring(
        'cd /Herwig/EventHandlers',
        'set LHEReader:PDFA /cmsPDFSet',
        'set LHEReader:PDFB /cmsPDFSet',
        'cd /',
    ),
    
    # Default settings for using POWHEG
    powhegDefaults = cms.vstring(
        # Need to use an NLO PDF
        'cp /Herwig/Partons/MRST-NLO /cmsPDFSet',
        'set /Herwig/Particles/p+:PDF    /Herwig/Partons/MRST-NLO',
        'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/MRST-NLO',
        # and strong coupling
        'create Herwig::O2AlphaS O2AlphaS',
        'set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS O2AlphaS',
        # Setup the POWHEG shower
        'cd /Herwig/Shower',
        # use the general recon for now
        'set KinematicsReconstructor:ReconstructionOption General',
        # create the Powheg evolver and use it instead of the default one
        'create Herwig::PowhegEvolver PowhegEvolver HwPowhegShower.so',
        'set ShowerHandler:Evolver PowhegEvolver',
        'set PowhegEvolver:ShowerModel ShowerModel',
        'set PowhegEvolver:SplittingGenerator SplittingGenerator',
        'set PowhegEvolver:MECorrMode 0',
        # create and use the Drell-yan hard emission generator
        'create Herwig::DrellYanHardGenerator DrellYanHardGenerator',
        'set DrellYanHardGenerator:ShowerAlpha AlphaQCD',
        'insert PowhegEvolver:HardGenerator 0 DrellYanHardGenerator',
        # create and use the gg->H hard emission generator
        'create Herwig::GGtoHHardGenerator GGtoHHardGenerator',
        'set GGtoHHardGenerator:ShowerAlpha AlphaQCD',
        'insert PowhegEvolver:HardGenerator 0 GGtoHHardGenerator',
    )
)

#HerwigppUE_EE_3C_cfi.py
herwigppUESettingsBlock = cms.PSet(
    herwigppUE_EE_3C_Base = cms.vstring(
        '+pdfCTEQ6L1',
        
        'cd /Herwig',
        'create Herwig::O2AlphaS O2AlphaS',
        'set Model:QCD/RunningAlphaS O2AlphaS',
        
        # Energy-independent MPI parameters
        #   Colour reconnection settings
        'set /Herwig/Hadronization/ColourReconnector:ColourReconnection Yes',
        'set /Herwig/Hadronization/ColourReconnector:ReconnectionProbability 0.54',
        #   Colour Disrupt settings
        'set /Herwig/Partons/RemnantDecayer:colourDisrupt 0.80',
        #   inverse hadron radius
        'set /Herwig/UnderlyingEvent/MPIHandler:InvRadius 1.11',
        #   MPI model settings
        #'set /Herwig/UnderlyingEvent/MPIHandler:IdenticalToUE 0',
        'set /Herwig/UnderlyingEvent/MPIHandler:softInt Yes',
        'set /Herwig/UnderlyingEvent/MPIHandler:twoComp Yes',
        'set /Herwig/UnderlyingEvent/MPIHandler:DLmode 2',
        'cd /',
    ),
    
    herwigppUE_EE_3C_900GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 900.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 1.55',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 3.1',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 1.81*GeV',
    ),
    
    herwigppUE_EE_3C_1800GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 1800.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 2.26',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 4.52',
    ),
    
    herwigppUE_EE_3C_2760GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 2760.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 2.33',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 4.66',
    ),

    # To calculate the values for 5.02 TeV 

    #root [35] minKT->Fit("fMinKT","","",1,14)
    #**************************************** 
    #Minimizer is Minuit / Migrad
    #Chi2                      =   0.00276018
    #NDf                       =            3
    #Edm                       =  5.16888e-26
    #NCalls                    =           34
    #p0                        =      2.04337   +/-   0.024943    
    #p1                        =     0.104444   +/-   0.00311857 
    #root [38] fMinKT->Eval(5.02)
    #(const Double_t)2.56768016533962795e+00 

    #root [37] MHatMin->Fit("fMHatMin","","",1,14)
    #****************************************
    #Minimizer is Minuit / Migrad
    #Chi2                      =    0.0110407
    #NDf                       =            3
    #Edm                       =   5.2017e-24
    #NCalls                    =           32
    #p0                        =      4.08674   +/-   0.0498861   
    #p1                        =     0.208889   +/-   0.00623715  
    #root [39] fMHatMin->Eval(5.02)
    #(const Double_t)5.13536033067979147e+00

    herwigppUE_EE_3C_5020GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 5020.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 2.5677',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 5.1354',
    ),
    
    herwigppUE_EE_3C_7000GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 2.752',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 5.504',
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.34*GeV',
    ),
    
    herwigppUE_EE_3C_8000GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 8000.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 2.85',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 5.7',
    ),
    
    herwigppUE_EE_3C_14000GeV = cms.vstring(
        '+herwigppUE_EE_3C_Base',
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0',
        'set /Herwig/UnderlyingEvent/KtCut:MinKT 3.53',
        'set /Herwig/UnderlyingEvent/UECuts:MHatMin 7.06',
    ),
)

process.generator = cms.EDFilter("ThePEGGeneratorFilter",
                                 herwigDefaultsBlock,
                                 herwigppUESettingsBlock,
                                 crossSection = cms.untracked.double(202900000),
                                 filterEfficiency = cms.untracked.double(1),
                                 
                                 configFiles = cms.vstring(),
                                 parameterSets = cms.vstring(
                                     'herwigppUE_EE_3C_7000GeV',
                                     'productionParameters',
                                     'basicSetup',
                                     'setParticlesStableForDetector',
                                 ),
                                 productionParameters = cms.vstring(
                                     'mkdir /Herwig/Weights',
                                     'cd /Herwig/Weights',
                                     'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so',
                                     
                                     'cd /Herwig/MatrixElements/',
                                     'insert SimpleQCD:MatrixElements[0] MEQCD2to2',
                                     'insert SimpleQCD:Preweights[0] /Herwig/Weights/reweightMinPT',
                                     
                                     'cd /',
                                     'set /Herwig/Weights/reweightMinPT:Power 4.5',
                                     'set /Herwig/Weights/reweightMinPT:Scale 15*GeV',
                                     'set /Herwig/Cuts/JetKtCut:MinKT '+ptmin+'*GeV', 
                                     'set /Herwig/Cuts/JetKtCut:MaxKT '+ptmax+'*GeV', 
                                     'set /Herwig/Cuts/QCDCuts:MHatMin 0.0*GeV', 
                                     'set /Herwig/UnderlyingEvent/MPIHandler:IdenticalToUE 0',
                                     'set /Herwig/Shower/ShowerHandler:MPIHandler NULL',
                                     'set /Herwig/EventHandlers/LHCHandler:HadronizationHandler NULL'
                                 ),
                             )

process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.generator * process.genParticles)

process.ak2GenJets = process.ak5GenJets.clone( rParam = 0.2 )
process.ak3GenJets = process.ak5GenJets.clone( rParam = 0.3 )
process.ak4GenJets = process.ak5GenJets.clone( rParam = 0.4 )
process.ak7GenJets = process.ak5GenJets.clone( rParam = 0.7 )

process.genjet_step = cms.Path(process.genJetParticles 
                               * process.ak2GenJets
                               * process.ak3GenJets
                               * process.ak4GenJets
                               * process.ak5GenJets
                               * process.ak7GenJets
                           )


# =============== Analysis =============================
process.ak3GenJetSpectrum = cms.EDAnalyzer('GenJetCrossCheckAnalyzer',
    genJetSrc = cms.InputTag("ak3GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    doCMatrix = cms.bool(True),
    doFlavor = cms.bool(False),
    flavorSrc = cms.InputTag("flavourByRef"),
    flavorId = cms.vint32(0),    
    jetsByAbsRapidity = cms.bool(False),
    etaMin = cms.double(-1.0),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.3),
    pthatMin = cms.double(options.ptHatLow),
    pthatMax = cms.double(options.ptHatHigh),
    ptBins = cms.vdouble( 3, 4, 5, 7, 9, 12, 15, 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,1000 ),
    pythiaProcess = cms.string(processType),
    dijetEtaBins = cms.vdouble( -3.01, -2.63333, -2.07, -1.78833, -1.50667, -1.225, -0.943333, -0.661667, -0.38, -0.0983333, 0.183333, 0.465, 0.746667, 1.02833, 1.31, 1.59167, 1.87333, 2.43667, 3.0),
    dijetEtaWeights = cms.vdouble( 1, 0.772085, 0.701301, 0.753585, 0.813741, 0.882849, 0.943137, 0.977332, 0.993655, 1.0375, 1.04713, 1.04826, 1.05517, 1.05983, 1.0723, 1.06945, 1.01587, 1.41731 )    
)

process.ak3GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum.clone(
    doCMatrix = cms.bool(False)
)
process.ak3GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(2.0)
)
process.ak3GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.5),
    etaMax = cms.double(-2.0)
)
process.ak3GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(-1.5)
)
process.ak3GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.5),
    etaMax = cms.double(-1.0)
)
process.ak3GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.0),
    etaMax = cms.double(-0.5)
)
process.ak3GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-0.5),
    etaMax = cms.double(0.5)
)
process.ak3GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0)
)
process.ak3GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5)
)
process.ak3GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0)
)

#R=0.2
process.ak2GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)

#R=0.4
process.ak4GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)

#R=0.5
process.ak5GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)

#R=0.7
process.ak7GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)



process.ana_step = cms.Path(
    process.ak3GenJetSpectrum_n10_p10 * 
    process.ak3GenJetSpectrum_n20_p20 *
    process.ak3GenJetSpectrum_n25_n20 *
    process.ak3GenJetSpectrum_n20_n15 *
    process.ak3GenJetSpectrum_n15_n10 *
    process.ak3GenJetSpectrum_n10_n05 *
    process.ak3GenJetSpectrum_n05_p05 *
    process.ak3GenJetSpectrum_p05_p10 *
    process.ak3GenJetSpectrum_p10_p15 *
    process.ak3GenJetSpectrum_p15_p20 *

    process.ak2GenJetSpectrum_n10_p10 * 
    process.ak2GenJetSpectrum_n20_p20 *
    process.ak2GenJetSpectrum_n25_n20 *
    process.ak2GenJetSpectrum_n20_n15 *
    process.ak2GenJetSpectrum_n15_n10 *
    process.ak2GenJetSpectrum_n10_n05 *
    process.ak2GenJetSpectrum_n05_p05 *
    process.ak2GenJetSpectrum_p05_p10 *
    process.ak2GenJetSpectrum_p10_p15 *
    process.ak2GenJetSpectrum_p15_p20 *

    process.ak4GenJetSpectrum_n10_p10 * 
    process.ak4GenJetSpectrum_n20_p20 *
    process.ak4GenJetSpectrum_n25_n20 *
    process.ak4GenJetSpectrum_n20_n15 *
    process.ak4GenJetSpectrum_n15_n10 *
    process.ak4GenJetSpectrum_n10_n05 *
    process.ak4GenJetSpectrum_n05_p05 *
    process.ak4GenJetSpectrum_p05_p10 *
    process.ak4GenJetSpectrum_p10_p15 *
    process.ak4GenJetSpectrum_p15_p20 *

    process.ak5GenJetSpectrum_n10_p10 * 
    process.ak5GenJetSpectrum_n20_p20 *
    process.ak5GenJetSpectrum_n25_n20 *
    process.ak5GenJetSpectrum_n20_n15 *
    process.ak5GenJetSpectrum_n15_n10 *
    process.ak5GenJetSpectrum_n10_n05 *
    process.ak5GenJetSpectrum_n05_p05 *
    process.ak5GenJetSpectrum_p05_p10 *
    process.ak5GenJetSpectrum_p10_p15 *
    process.ak5GenJetSpectrum_p15_p20 *

    process.ak7GenJetSpectrum_n10_p10 * 
    process.ak7GenJetSpectrum_n20_p20 *
    process.ak7GenJetSpectrum_n25_n20 *
    process.ak7GenJetSpectrum_n20_n15 *
    process.ak7GenJetSpectrum_n15_n10 *
    process.ak7GenJetSpectrum_n10_n05 *
    process.ak7GenJetSpectrum_n05_p05 *
    process.ak7GenJetSpectrum_p05_p10 *
    process.ak7GenJetSpectrum_p10_p15 *
    process.ak7GenJetSpectrum_p15_p20 
)

process.endjob_step = cms.Path(process.endOfProcess)
#process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step, process.genjet_step,process.ana_step,process.endjob_step)

# special treatment in case of production filter sequence  
for path in process.paths: 
    getattr(process,path)._seq = process.ProductionFilterSequence*getattr(process,path)._seq


# Automatic addition of the customisation function

def customise(process):
    process.genParticles.abortOnUnknownPDGCode = False

    return(process)


# End of customisation function definition

process = customise(process)

