#!/usr/bin/env python

#
# Generated Tue Dec 11 20:12:28 2012 by generateDS.py version 2.7c.
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class sixfivezerotwoSub(supermod.sixfivezerotwo):
    def __init__(self, annotation=None, lineGroup=None):
        super(sixfivezerotwoSub, self).__init__(annotation, lineGroup, )
supermod.sixfivezerotwo.subclass = sixfivezerotwoSub
# end class sixfivezerotwoSub


class labelSub(supermod.label):
    def __init__(self, name=None, lineGroup=None):
        super(labelSub, self).__init__(name, lineGroup, )
supermod.label.subclass = labelSub
# end class labelSub


class mnemonicSub(supermod.mnemonic):
    def __init__(self, ADCaddWithCarry=None, ANDbitwiseAndWithAccumulator=None, ASLartihmeticShiftLeft=None, BITtestBits=None, BPLsetCarry=None, BMIbranchonMinus=None, BVCbranchonOverflowClear=None, BVSbranchonOverflowSet=None, BCCbranchonCarryClear=None, BCSbranchonCarrySet=None, BEQbranchonEqual=None, BNEbranchonNotequal=None, BRKbreak=None, CMPcompareAccumulator=None, CPXcompareXRegister=None, CPYcompareYRegister=None, DECdecrementMemory=None, EORbitWiseExclusiveOr=None, CLClearCarry=None, SECsetCarry=None, SEIsetCarry=None, CLIclearInterrupt=None, SEIsetInterrupt=None, CLVclearOverflow=None, CLDclearDecimal=None, SEDsetDecimal=None, INCincrementMemory=None, JMPjump=None, JSRjumpToSubRoutine=None, LDAloadAccumulator=None, LDXloadXRegister=None, LDYloadYRegister=None, LSRlogicalShiftRight=None, NOPnoOperation=None, ORAbitwiseOrWithAccumulator=None, TAXTtansferAtoX=None, TXAtransferXtoA=None, DEXdecrementX=None, INXincrementX=None, TAYtransferAtoY=None, DEYdecrementY=None, INYincrementY=None, ROLrotateLeft=None, RORrotateRight=None, RTIreturnFromInterrupt=None, RTSreturnFromSubroutine=None, SBCSubTractwithCarry=None, STAStoreAccumulator=None, TSXTransferXtoStackptr=None, TSXTranferStackPtrtoX=None, PHAPushAccumulator=None, PLApullAccumulator=None, PHPpushProcessorStatus=None, PLPpullProcessorsStatus=None, STXstoreXReigster=None, STYstoreYRegister=None):
        super(mnemonicSub, self).__init__(ADCaddWithCarry, ANDbitwiseAndWithAccumulator, ASLartihmeticShiftLeft, BITtestBits, BPLsetCarry, BMIbranchonMinus, BVCbranchonOverflowClear, BVSbranchonOverflowSet, BCCbranchonCarryClear, BCSbranchonCarrySet, BEQbranchonEqual, BNEbranchonNotequal, BRKbreak, CMPcompareAccumulator, CPXcompareXRegister, CPYcompareYRegister, DECdecrementMemory, EORbitWiseExclusiveOr, CLClearCarry, SECsetCarry, SEIsetCarry, CLIclearInterrupt, SEIsetInterrupt, CLVclearOverflow, CLDclearDecimal, SEDsetDecimal, INCincrementMemory, JMPjump, JSRjumpToSubRoutine, LDAloadAccumulator, LDXloadXRegister, LDYloadYRegister, LSRlogicalShiftRight, NOPnoOperation, ORAbitwiseOrWithAccumulator, TAXTtansferAtoX, TXAtransferXtoA, DEXdecrementX, INXincrementX, TAYtransferAtoY, DEYdecrementY, INYincrementY, ROLrotateLeft, RORrotateRight, RTIreturnFromInterrupt, RTSreturnFromSubroutine, SBCSubTractwithCarry, STAStoreAccumulator, TSXTransferXtoStackptr, TSXTranferStackPtrtoX, PHAPushAccumulator, PLApullAccumulator, PHPpushProcessorStatus, PLPpullProcessorsStatus, STXstoreXReigster, STYstoreYRegister, )
supermod.mnemonic.subclass = mnemonicSub
# end class mnemonicSub


class ADCaddWithCarrySub(supermod.ADCaddWithCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(ADCaddWithCarrySub, self).__init__(name, value, comment, )
supermod.ADCaddWithCarry.subclass = ADCaddWithCarrySub
# end class ADCaddWithCarrySub


class ANDbitwiseAndWithAccumulatorSub(supermod.ANDbitwiseAndWithAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(ANDbitwiseAndWithAccumulatorSub, self).__init__(name, value, comment, )
supermod.ANDbitwiseAndWithAccumulator.subclass = ANDbitwiseAndWithAccumulatorSub
# end class ANDbitwiseAndWithAccumulatorSub


class ASLartihmeticShiftLeftSub(supermod.ASLartihmeticShiftLeft):
    def __init__(self, name=None, value=None, comment=None):
        super(ASLartihmeticShiftLeftSub, self).__init__(name, value, comment, )
supermod.ASLartihmeticShiftLeft.subclass = ASLartihmeticShiftLeftSub
# end class ASLartihmeticShiftLeftSub


class BITtestBitsSub(supermod.BITtestBits):
    def __init__(self, name=None, value=None, comment=None):
        super(BITtestBitsSub, self).__init__(name, value, comment, )
supermod.BITtestBits.subclass = BITtestBitsSub
# end class BITtestBitsSub


class BPLsetCarrySub(supermod.BPLsetCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(BPLsetCarrySub, self).__init__(name, value, comment, )
supermod.BPLsetCarry.subclass = BPLsetCarrySub
# end class BPLsetCarrySub


class BMIbranchonMinusSub(supermod.BMIbranchonMinus):
    def __init__(self, name=None, value=None, comment=None):
        super(BMIbranchonMinusSub, self).__init__(name, value, comment, )
supermod.BMIbranchonMinus.subclass = BMIbranchonMinusSub
# end class BMIbranchonMinusSub


class BVCbranchonOverflowClearSub(supermod.BVCbranchonOverflowClear):
    def __init__(self, name=None, value=None, comment=None):
        super(BVCbranchonOverflowClearSub, self).__init__(name, value, comment, )
supermod.BVCbranchonOverflowClear.subclass = BVCbranchonOverflowClearSub
# end class BVCbranchonOverflowClearSub


class BVSbranchonOverflowSetSub(supermod.BVSbranchonOverflowSet):
    def __init__(self, name=None, value=None, comment=None):
        super(BVSbranchonOverflowSetSub, self).__init__(name, value, comment, )
supermod.BVSbranchonOverflowSet.subclass = BVSbranchonOverflowSetSub
# end class BVSbranchonOverflowSetSub


class BCCbranchonCarryClearSub(supermod.BCCbranchonCarryClear):
    def __init__(self, name=None, value=None, comment=None):
        super(BCCbranchonCarryClearSub, self).__init__(name, value, comment, )
supermod.BCCbranchonCarryClear.subclass = BCCbranchonCarryClearSub
# end class BCCbranchonCarryClearSub


class BCSbranchonCarrySetSub(supermod.BCSbranchonCarrySet):
    def __init__(self, name=None, value=None, comment=None):
        super(BCSbranchonCarrySetSub, self).__init__(name, value, comment, )
supermod.BCSbranchonCarrySet.subclass = BCSbranchonCarrySetSub
# end class BCSbranchonCarrySetSub


class BEQbranchonEqualSub(supermod.BEQbranchonEqual):
    def __init__(self, name=None, value=None, comment=None):
        super(BEQbranchonEqualSub, self).__init__(name, value, comment, )
supermod.BEQbranchonEqual.subclass = BEQbranchonEqualSub
# end class BEQbranchonEqualSub


class BNEbranchonNotequalSub(supermod.BNEbranchonNotequal):
    def __init__(self, name=None, value=None, comment=None):
        super(BNEbranchonNotequalSub, self).__init__(name, value, comment, )
supermod.BNEbranchonNotequal.subclass = BNEbranchonNotequalSub
# end class BNEbranchonNotequalSub


class BRKbreakSub(supermod.BRKbreak):
    def __init__(self, name=None, value=None, comment=None):
        super(BRKbreakSub, self).__init__(name, value, comment, )
supermod.BRKbreak.subclass = BRKbreakSub
# end class BRKbreakSub


class CMPcompareAccumulatorSub(supermod.CMPcompareAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(CMPcompareAccumulatorSub, self).__init__(name, value, comment, )
supermod.CMPcompareAccumulator.subclass = CMPcompareAccumulatorSub
# end class CMPcompareAccumulatorSub


class CPXcompareXRegisterSub(supermod.CPXcompareXRegister):
    def __init__(self, name=None, value=None, comment=None):
        super(CPXcompareXRegisterSub, self).__init__(name, value, comment, )
supermod.CPXcompareXRegister.subclass = CPXcompareXRegisterSub
# end class CPXcompareXRegisterSub


class CPYcompareYRegisterSub(supermod.CPYcompareYRegister):
    def __init__(self, name=None, value=None, comment=None):
        super(CPYcompareYRegisterSub, self).__init__(name, value, comment, )
supermod.CPYcompareYRegister.subclass = CPYcompareYRegisterSub
# end class CPYcompareYRegisterSub


class DECdecrementMemorySub(supermod.DECdecrementMemory):
    def __init__(self, name=None, value=None, comment=None):
        super(DECdecrementMemorySub, self).__init__(name, value, comment, )
supermod.DECdecrementMemory.subclass = DECdecrementMemorySub
# end class DECdecrementMemorySub


class EORbitWiseExclusiveOrSub(supermod.EORbitWiseExclusiveOr):
    def __init__(self, name=None, value=None, comment=None):
        super(EORbitWiseExclusiveOrSub, self).__init__(name, value, comment, )
supermod.EORbitWiseExclusiveOr.subclass = EORbitWiseExclusiveOrSub
# end class EORbitWiseExclusiveOrSub


class CLClearCarrySub(supermod.CLClearCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(CLClearCarrySub, self).__init__(name, value, comment, )
supermod.CLClearCarry.subclass = CLClearCarrySub
# end class CLClearCarrySub


class SECsetCarrySub(supermod.SECsetCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(SECsetCarrySub, self).__init__(name, value, comment, )
supermod.SECsetCarry.subclass = SECsetCarrySub
# end class SECsetCarrySub


class SEIsetCarrySub(supermod.SEIsetCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(SEIsetCarrySub, self).__init__(name, value, comment, )
supermod.SEIsetCarry.subclass = SEIsetCarrySub
# end class SEIsetCarrySub


class CLIclearInterruptSub(supermod.CLIclearInterrupt):
    def __init__(self, name=None, value=None, comment=None):
        super(CLIclearInterruptSub, self).__init__(name, value, comment, )
supermod.CLIclearInterrupt.subclass = CLIclearInterruptSub
# end class CLIclearInterruptSub


class SEIsetInterruptSub(supermod.SEIsetInterrupt):
    def __init__(self, name=None, value=None, comment=None):
        super(SEIsetInterruptSub, self).__init__(name, value, comment, )
supermod.SEIsetInterrupt.subclass = SEIsetInterruptSub
# end class SEIsetInterruptSub


class CLVclearOverflowSub(supermod.CLVclearOverflow):
    def __init__(self, name=None, value=None, comment=None):
        super(CLVclearOverflowSub, self).__init__(name, value, comment, )
supermod.CLVclearOverflow.subclass = CLVclearOverflowSub
# end class CLVclearOverflowSub


class CLDclearDecimalSub(supermod.CLDclearDecimal):
    def __init__(self, name=None, value=None, comment=None):
        super(CLDclearDecimalSub, self).__init__(name, value, comment, )
supermod.CLDclearDecimal.subclass = CLDclearDecimalSub
# end class CLDclearDecimalSub


class SEDsetDecimalSub(supermod.SEDsetDecimal):
    def __init__(self, name=None, value=None, comment=None):
        super(SEDsetDecimalSub, self).__init__(name, value, comment, )
supermod.SEDsetDecimal.subclass = SEDsetDecimalSub
# end class SEDsetDecimalSub


class INCincrementMemorySub(supermod.INCincrementMemory):
    def __init__(self, name=None, value=None, comment=None):
        super(INCincrementMemorySub, self).__init__(name, value, comment, )
supermod.INCincrementMemory.subclass = INCincrementMemorySub
# end class INCincrementMemorySub


class JMPjumpSub(supermod.JMPjump):
    def __init__(self, name=None, value=None, comment=None):
        super(JMPjumpSub, self).__init__(name, value, comment, )
supermod.JMPjump.subclass = JMPjumpSub
# end class JMPjumpSub


class JSRjumpToSubRoutineSub(supermod.JSRjumpToSubRoutine):
    def __init__(self, name=None, value=None, comment=None):
        super(JSRjumpToSubRoutineSub, self).__init__(name, value, comment, )
supermod.JSRjumpToSubRoutine.subclass = JSRjumpToSubRoutineSub
# end class JSRjumpToSubRoutineSub


class LDAloadAccumulatorSub(supermod.LDAloadAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(LDAloadAccumulatorSub, self).__init__(name, value, comment, )
supermod.LDAloadAccumulator.subclass = LDAloadAccumulatorSub
# end class LDAloadAccumulatorSub


class LDXloadXRegisterSub(supermod.LDXloadXRegister):
    def __init__(self, name=None, value=None, comment=None):
        super(LDXloadXRegisterSub, self).__init__(name, value, comment, )
supermod.LDXloadXRegister.subclass = LDXloadXRegisterSub
# end class LDXloadXRegisterSub


class LDYloadYRegisterSub(supermod.LDYloadYRegister):
    def __init__(self, name=None, value=None, comment=None):
        super(LDYloadYRegisterSub, self).__init__(name, value, comment, )
supermod.LDYloadYRegister.subclass = LDYloadYRegisterSub
# end class LDYloadYRegisterSub


class LSRlogicalShiftRightSub(supermod.LSRlogicalShiftRight):
    def __init__(self, name=None, value=None, comment=None):
        super(LSRlogicalShiftRightSub, self).__init__(name, value, comment, )
supermod.LSRlogicalShiftRight.subclass = LSRlogicalShiftRightSub
# end class LSRlogicalShiftRightSub


class NOPnoOperationSub(supermod.NOPnoOperation):
    def __init__(self, name=None, value=None, comment=None):
        super(NOPnoOperationSub, self).__init__(name, value, comment, )
supermod.NOPnoOperation.subclass = NOPnoOperationSub
# end class NOPnoOperationSub


class ORAbitwiseOrWithAccumulatorSub(supermod.ORAbitwiseOrWithAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(ORAbitwiseOrWithAccumulatorSub, self).__init__(name, value, comment, )
supermod.ORAbitwiseOrWithAccumulator.subclass = ORAbitwiseOrWithAccumulatorSub
# end class ORAbitwiseOrWithAccumulatorSub


class TAXTtansferAtoXSub(supermod.TAXTtansferAtoX):
    def __init__(self, name=None, value=None, comment=None):
        super(TAXTtansferAtoXSub, self).__init__(name, value, comment, )
supermod.TAXTtansferAtoX.subclass = TAXTtansferAtoXSub
# end class TAXTtansferAtoXSub


class TXAtransferXtoASub(supermod.TXAtransferXtoA):
    def __init__(self, name=None, value=None, comment=None):
        super(TXAtransferXtoASub, self).__init__(name, value, comment, )
supermod.TXAtransferXtoA.subclass = TXAtransferXtoASub
# end class TXAtransferXtoASub


class DEXdecrementXSub(supermod.DEXdecrementX):
    def __init__(self, name=None, value=None, comment=None):
        super(DEXdecrementXSub, self).__init__(name, value, comment, )
supermod.DEXdecrementX.subclass = DEXdecrementXSub
# end class DEXdecrementXSub


class INXincrementXSub(supermod.INXincrementX):
    def __init__(self, name=None, value=None, comment=None):
        super(INXincrementXSub, self).__init__(name, value, comment, )
supermod.INXincrementX.subclass = INXincrementXSub
# end class INXincrementXSub


class TAYtransferAtoYSub(supermod.TAYtransferAtoY):
    def __init__(self, name=None, value=None, comment=None):
        super(TAYtransferAtoYSub, self).__init__(name, value, comment, )
supermod.TAYtransferAtoY.subclass = TAYtransferAtoYSub
# end class TAYtransferAtoYSub


class DEYdecrementYSub(supermod.DEYdecrementY):
    def __init__(self, name=None, value=None, comment=None):
        super(DEYdecrementYSub, self).__init__(name, value, comment, )
supermod.DEYdecrementY.subclass = DEYdecrementYSub
# end class DEYdecrementYSub


class INYincrementYSub(supermod.INYincrementY):
    def __init__(self, name=None, value=None, comment=None):
        super(INYincrementYSub, self).__init__(name, value, comment, )
supermod.INYincrementY.subclass = INYincrementYSub
# end class INYincrementYSub


class ROLrotateLeftSub(supermod.ROLrotateLeft):
    def __init__(self, name=None, value=None, comment=None):
        super(ROLrotateLeftSub, self).__init__(name, value, comment, )
supermod.ROLrotateLeft.subclass = ROLrotateLeftSub
# end class ROLrotateLeftSub


class RORrotateRightSub(supermod.RORrotateRight):
    def __init__(self, name=None, value=None, comment=None):
        super(RORrotateRightSub, self).__init__(name, value, comment, )
supermod.RORrotateRight.subclass = RORrotateRightSub
# end class RORrotateRightSub


class RTIreturnFromInterruptSub(supermod.RTIreturnFromInterrupt):
    def __init__(self, name=None, value=None, comment=None):
        super(RTIreturnFromInterruptSub, self).__init__(name, value, comment, )
supermod.RTIreturnFromInterrupt.subclass = RTIreturnFromInterruptSub
# end class RTIreturnFromInterruptSub


class RTSreturnFromSubroutineSub(supermod.RTSreturnFromSubroutine):
    def __init__(self, name=None, value=None, comment=None):
        super(RTSreturnFromSubroutineSub, self).__init__(name, value, comment, )
supermod.RTSreturnFromSubroutine.subclass = RTSreturnFromSubroutineSub
# end class RTSreturnFromSubroutineSub


class SBCSubTractwithCarrySub(supermod.SBCSubTractwithCarry):
    def __init__(self, name=None, value=None, comment=None):
        super(SBCSubTractwithCarrySub, self).__init__(name, value, comment, )
supermod.SBCSubTractwithCarry.subclass = SBCSubTractwithCarrySub
# end class SBCSubTractwithCarrySub


class STAStoreAccumulatorSub(supermod.STAStoreAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(STAStoreAccumulatorSub, self).__init__(name, value, comment, )
supermod.STAStoreAccumulator.subclass = STAStoreAccumulatorSub
# end class STAStoreAccumulatorSub


class TSXTransferXtoStackptrSub(supermod.TSXTransferXtoStackptr):
    def __init__(self, name=None, value=None, comment=None):
        super(TSXTransferXtoStackptrSub, self).__init__(name, value, comment, )
supermod.TSXTransferXtoStackptr.subclass = TSXTransferXtoStackptrSub
# end class TSXTransferXtoStackptrSub


class TSXTranferStackPtrtoXSub(supermod.TSXTranferStackPtrtoX):
    def __init__(self, name=None, value=None, comment=None):
        super(TSXTranferStackPtrtoXSub, self).__init__(name, value, comment, )
supermod.TSXTranferStackPtrtoX.subclass = TSXTranferStackPtrtoXSub
# end class TSXTranferStackPtrtoXSub


class PHAPushAccumulatorSub(supermod.PHAPushAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(PHAPushAccumulatorSub, self).__init__(name, value, comment, )
supermod.PHAPushAccumulator.subclass = PHAPushAccumulatorSub
# end class PHAPushAccumulatorSub


class PLApullAccumulatorSub(supermod.PLApullAccumulator):
    def __init__(self, name=None, value=None, comment=None):
        super(PLApullAccumulatorSub, self).__init__(name, value, comment, )
supermod.PLApullAccumulator.subclass = PLApullAccumulatorSub
# end class PLApullAccumulatorSub


class PHPpushProcessorStatusSub(supermod.PHPpushProcessorStatus):
    def __init__(self, name=None, value=None, comment=None):
        super(PHPpushProcessorStatusSub, self).__init__(name, value, comment, )
supermod.PHPpushProcessorStatus.subclass = PHPpushProcessorStatusSub
# end class PHPpushProcessorStatusSub


class PLPpullProcessorsStatusSub(supermod.PLPpullProcessorsStatus):
    def __init__(self, name=None, value=None, comment=None):
        super(PLPpullProcessorsStatusSub, self).__init__(name, value, comment, )
supermod.PLPpullProcessorsStatus.subclass = PLPpullProcessorsStatusSub
# end class PLPpullProcessorsStatusSub


class STXstoreXReigsterSub(supermod.STXstoreXReigster):
    def __init__(self, name=None, value=None, comment=None):
        super(STXstoreXReigsterSub, self).__init__(name, value, comment, )
supermod.STXstoreXReigster.subclass = STXstoreXReigsterSub
# end class STXstoreXReigsterSub


class STYstoreYRegisterSub(supermod.STYstoreYRegister):
    def __init__(self, name=None, value=None, comment=None):
        super(STYstoreYRegisterSub, self).__init__(name, value, comment, )
supermod.STYstoreYRegister.subclass = STYstoreYRegisterSub
# end class STYstoreYRegisterSub


class lineGroupSub(supermod.lineGroup):
    def __init__(self, line=None, multiLineComment=None):
        super(lineGroupSub, self).__init__(line, multiLineComment, )
supermod.lineGroup.subclass = lineGroupSub
# end class lineGroupSub


class lineSub(supermod.line):
    def __init__(self, mnemonic=None, label=None):
        super(lineSub, self).__init__(mnemonic, label, )
supermod.line.subclass = lineSub
# end class lineSub


class annotationSub(supermod.annotation):
    def __init__(self, emph=None, term=None, cited=None, ital=None, bold=None, valueOf_=None, mixedclass_=None, content_=None):
        super(annotationSub, self).__init__(emph, term, cited, ital, bold, valueOf_, mixedclass_, content_, )
supermod.annotation.subclass = annotationSub
# end class annotationSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sixfivezerotwo'
        rootClass = supermod.sixfivezerotwo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sixfivezerotwo'
        rootClass = supermod.sixfivezerotwo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sixfivezerotwo'
        rootClass = supermod.sixfivezerotwo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.sixfivezerotwo(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="sixfivezerotwo")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


