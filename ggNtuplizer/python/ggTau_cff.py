import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.producersLayer1.tauProducer_cfi import *
patTaus.tauIDSources.byLooseElectronRejection          = cms.InputTag("hpsPFTauDiscriminationByLooseElectronRejection")
patTaus.tauIDSources.byMediumElectronRejection         = cms.InputTag("hpsPFTauDiscriminationByMediumElectronRejection")
patTaus.tauIDSources.byTightElectronRejection 	    =    cms.InputTag("hpsPFTauDiscriminationByTightElectronRejection")
patTaus.tauIDSources.byMVA3VTightElectronRejection =     cms.InputTag("hpsPFTauDiscriminationByMVA5VTightElectronRejection")
patTaus.tauIDSources.byLooseMuonRejection              = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection")
patTaus.tauIDSources.byMediumMuonRejection             = cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection")
patTaus.tauIDSources.byTightMuonRejection              = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection")
patTaus.tauIDSources.byLooseMuonRejection3             = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection3")
patTaus.tauIDSources.byTightMuonRejection3             = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection3")
patTaus.tauIDSources.byMVArawMuonRejection             = cms.InputTag("hpsPFTauDiscriminationByMVArawMuonRejection")
patTaus.tauIDSources.byDecayModeFinding                = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
patTaus.tauIDSources.byVLooseIsolation                 = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolation")
patTaus.tauIDSources.byVLooseCombinedIsolationDBSumPtCorr  = cms.InputTag("hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr")
patTaus.tauIDSources.byLooseCombinedIsolationDBSumPtCorr   = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr")
patTaus.tauIDSources.byMediumCombinedIsolationDBSumPtCorr  = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr")
patTaus.tauIDSources.byTightCombinedIsolationDBSumPtCorr   = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr")
patTaus.tauIDSources.byLooseCombinedIsolationDBSumPtCorr3Hits =cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits")
patTaus.tauIDSources.byMediumCombinedIsolationDBSumPtCorr3Hits=cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits")
patTaus.tauIDSources.byTightCombinedIsolationDBSumPtCorr3Hits=cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits")