##
# Return the function to be used to check if an ele passes the BDT cut, pre-configured for:
# - era (2018, 2022...)
# - dataTag ('UL', etc)
# - nanoAOD version (9, ecc)
##

def getEleBDTCut(era, dataTag, nanoVersion, useUncorrPt=False) :
    # nanoAODv9 includes mvaFall17V2Iso = 2017 WP and training (ElectronMVAEstimatorRun2Fall17IsoV2Values)

    def eleBDTCut_RunIIpreUL_v9(ele) :
        # pre-UL WP for Run II (miniAOD branch: Run2_CutBased_BTag16)
        fSCeta = abs(ele.eta + ele.deltaEtaSC)
        BDT = ele.mvaFall17V2Iso
        return (ele.pt<=10. and     ((fSCeta<0.8                   and BDT > 0.85216885148) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.82684550976) or \
                                     (fSCeta>=1.479                and BDT > 0.86937630022))) \
                or (ele.pt>10. and  ((fSCeta<0.8                   and BDT > 0.98248928759) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.96919224579) or \
                                     (fSCeta>=1.479                and BDT > 0.79349796445)))
  
    def eleBDTCut_RunIIUL_v9(ele) :
        # UL WP (miniAOD branch Run2_CutBased_UL)
        fSCeta = abs(ele.eta + ele.deltaEtaSC)
        BDT = ele.mvaFall17V2Iso
        return (ele.pt<=10. and     ((fSCeta<0.8                   and BDT > 0.9128577458) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.9056792368) or \
                                     (fSCeta>=1.479                and BDT > 0.9439440575))) \
                or (ele.pt>10. and  ((fSCeta<0.8                   and BDT > 0.1559788054) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.0273863727) or \
                                     (fSCeta>=1.479                and BDT > -0.5532483665)))

    # Run2 UL HZZ WPs for 2016, 2017, 2018

    def eleBDTCut_RunIIUL_HZZ_2016(ele) :
        fSCeta = abs(ele.eta + ele.deltaEtaSC)
        BDT = ele.mvaHZZIso
        return (ele.pt<=10. and     ((fSCeta<0.8                   and BDT > 1.8949071018) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 1.80714210202) or \
                                     (fSCeta>=1.479                and BDT > 1.64751528517))) \
                or (ele.pt>10. and  ((fSCeta<0.8                   and BDT > 0.339697782473) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.252039219555) or \
                                     (fSCeta>=1.479                and BDT > -0.686263559006)))

    def eleBDTCut_RunIIUL_HZZ_2017(ele) :
        fSCeta = abs(ele.eta + ele.deltaEtaSC)
        BDT = ele.mvaHZZIso
        return (ele.pt<=10. and     ((fSCeta<0.8                   and BDT > 1.54440585808) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 1.50294621563) or \
                                     (fSCeta>=1.479                and BDT > 1.77306202112))) \
                or (ele.pt>10. and  ((fSCeta<0.8                   and BDT > 0.157262554087) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.0273932225081) or \
                                     (fSCeta>=1.479                and BDT > -0.623050463489)))
    
    def eleBDTCut_RunIIUL_HZZ_2018(ele) :
        fSCeta = abs(ele.eta + ele.deltaEtaSC)
        BDT = ele.mvaHZZIso
        return (ele.pt<=10. and     ((fSCeta<0.8                   and BDT > 1.49603193295) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 1.52414154008) or \
                                     (fSCeta>=1.479                and BDT > 1.77694249574))) \
                or (ele.pt>10. and  ((fSCeta<0.8                   and BDT > 0.199463934736) or \
                                     (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.076063564084) or \
                                     (fSCeta>=1.479                and BDT > -0.572118857519)))

    # Run3 nanoAODv12 samples have the 2018 UL tuning (ElectronMVAEstimatorRun2Summer18ULIdIsoValues)
    # The WP was derived before scale corrections, so the uncorrected pt should be used when available.
    def eleBDTCut_RunIII_ULTraining_def(ele) :
        return(eleBDTCut_RunIII_ULTraining(ele.pt, abs(ele.eta + ele.deltaEtaSC), ele.mvaHZZIso))
        
    def eleBDTCut_RunIII_ULTraining_uncorr(ele) :
        return(eleBDTCut_RunIII_ULTraining(ele.uncorrected_pt, abs(ele.eta + ele.deltaEtaSC), ele.mvaHZZIso))
               
    def eleBDTCut_RunIII_ULTraining(pt, fSCeta, BDT) :
        return (pt<=10. and     ((fSCeta<0.8                   and BDT > 0.9044286167) or \
                                 (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.9094166886) or \
                                 (fSCeta>=1.479                and BDT > 0.9443653660))) \
               or (pt>10. and  ((fSCeta<0.8                   and BDT > 0.1968600840) or \
                                (fSCeta>=0.8 and fSCeta<1.479 and BDT > 0.0759172100) or \
                                (fSCeta>=1.479                and BDT > -0.5169136775)))

    if era == 2017 or era == 2018 or era == 2016 :
        if "UL" in dataTag :
            if nanoVersion <10 :
                return eleBDTCut_RunIIUL_v9
            else:
                if era == 2016 :
                    return eleBDTCut_RunIIUL_HZZ_2016
                elif era == 2017 :
                    return eleBDTCut_RunIIUL_HZZ_2017
                elif era == 2018 :
                    return eleBDTCut_RunIIUL_HZZ_2018
        else :
            if nanoVersion <10 :
                return eleBDTCut_RunIIpreUL_v9

    elif era >=2022 :
        if useUncorrPt:
            print("unc")
            return eleBDTCut_RunIII_ULTraining_uncorr
        else :
            return eleBDTCut_RunIII_ULTraining_def

    # Fallback: combination not supported
    raise ValueError('getEleBDTCut: era '+ str(era)+', dataTag ' + dataTag + ', nanoVersion ' + nanoVersion + ' not supported')


