import ROOT

#loading up to 10 root files from a root tree and gives out the hists
#input: FileName,histName1,histName2,histName3,histName4,histName5,histName6,histName7,histName8,histName9,histName10
#output: hist1,hist2,hist3,hist4,hist5,hist6,hist7,hist8,hist9,hist10
def loadRootFiles(FileName,histName1=None,histName2=None,histName3=None,histName4=None,histName5=None,histName6=None,histName7=None,histName8=None,histName9=None,histName10=None):
    histFile = ROOT.TFile.Open(FileName,"READ")

    if histName1 != None:
        hist1 = histFile.Get(histName1)
        hist1.SetDirectory(0)
    else:
        hist1 = None
    if histName2 != None:
        hist2 = histFile.Get(histName2)
        hist2.SetDirectory(0)
    else:
        hist2 = None
    if histName3 != None:
        hist3 = histFile.Get(histName3)
        hist3.SetDirectory(0)
    else:
        hist3 = None
    if histName4 != None:
        hist4 = histFile.Get(histName4)
        hist4.SetDirectory(0)
    else:
        hist4 = None
    if histName5 != None:
        hist5 = histFile.Get(histName5)
        hist5.SetDirectory(0)
    else:
        hist5 = None
    if histName6 != None:
        hist6 = histFile.Get(histName6)
        hist6.SetDirectory(0)
    else:
        hist6 = None
    if histName7 != None:
        hist7 = histFile.Get(histName7)
        hist7.SetDirectory(0)
    else:
        hist7 = None
    if histName8 != None:
        hist8 = histFile.Get(histName8)
        hist8.SetDirectory(0)
    else:
        hist8 = None
    if histName9 != None:
        hist9 = histFile.Get(histName9)
        hist9.SetDirectory(0)
    else:
        hist9 = None
    if histName10 != None:
        hist10 = histFile.Get(histName10)
        hist10.SetDirectory(0)
    else:
        hist10 = None

    histFile.Close()
    print(FileName+" is loaded")
    return hist1,hist2,hist3,hist4,hist5,hist6,hist7,hist8,hist9,hist10

#takes data array of hists and vconverts them into pdf files with custom design settings
#input: outFileName,data,titlesArray,xAxisTitle,yAxisTitle
#output: creates pdf file in outFileName
def RootHisttoPdf(outFileName,data1,data2,data3,titlesArray,xAxisTitle,yAxisTitle,histNum,logyScale):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1[0],"jet1 data")
    legend.AddEntry(data2[0],"jet2 data")
    legend.AddEntry(data3[0],"jet3 data")

    canvas.Print(outFileName+"[")
    for i in range(0,histNum):
        data1[i].SetStats(0)
        data1[i].SetLineColor(ROOT.kBlack)
        data1[i].SetLineWidth(2)
        data2[i].SetStats(0)
        data2[i].SetLineColor(ROOT.kBlue)
        data2[i].SetLineWidth(2)
        data3[i].SetStats(0)
        data3[i].SetLineColor(ROOT.kRed)
        data3[i].SetLineWidth(2)
        data1[i].GetYaxis().SetTitle(yAxisTitle)
        data1[i].GetXaxis().SetTitle(xAxisTitle)
        data1[i].SetTitle("")
        data2[i].SetTitle("")
        data3[i].SetTitle("")
        data1[i].Draw("pe")
        data2[i].Draw("pe,same")
        data3[i].Draw("pe,same")
        legend.Draw("same")
        latex.DrawText(0.5,0.8,titlesArray[i])
        canvas.Print(outFileName)
    canvas.Print(outFileName+"]")

#loads hists and create pdf files for certain quantity
def loadAndSave(inDirectory,outDirectory,histNum,variable,xAxis,setLogy=False):
    Jet1Hist1,Jet1Hist2,Jet1Hist3,Jet1Hist4,Jet1Hist5,Jet1Hist6,Jet1Hist7,Jet1Hist8,Jet1Hist9,Jet1Hist10 = loadRootFiles(inDirectory+variable+"1hists.root",variable+"1allmjjvaluesHist",variable+"1250to350Hist",variable+"1350to500Hist",variable+"1500to650Hist",variable+"1650to850Hist",variable+"1850to1100Hist",variable+"11100to1400Hist",variable+"11400to1800Hist",variable+"11800to2200Hist",variable+"1over2200Hist")
    Jet2Hist1,Jet2Hist2,Jet2Hist3,Jet2Hist4,Jet2Hist5,Jet2Hist6,Jet2Hist7,Jet2Hist8,Jet2Hist9,Jet2Hist10 = loadRootFiles(inDirectory+variable+"2hists.root",variable+"2allmjjvaluesHist",variable+"2250to350Hist",variable+"2350to500Hist",variable+"2500to650Hist",variable+"2650to850Hist",variable+"2850to1100Hist",variable+"21100to1400Hist",variable+"21400to1800Hist",variable+"21800to2200Hist",variable+"2over2200Hist")
    Jet3Hist1,Jet3Hist2,Jet3Hist3,Jet3Hist4,Jet3Hist5,Jet3Hist6,Jet3Hist7,Jet3Hist8,Jet3Hist9,Jet3Hist10 = loadRootFiles(inDirectory+variable+"3hists.root",variable+"3allmjjvaluesHist",variable+"3250to350Hist",variable+"3350to500Hist",variable+"3500to650Hist",variable+"3650to850Hist",variable+"3850to1100Hist",variable+"31100to1400Hist",variable+"31400to1800Hist",variable+"31800to2200Hist",variable+"3over2200Hist")
    Jet1HistArray = [Jet1Hist1,Jet1Hist2,Jet1Hist3,Jet1Hist4,Jet1Hist5,Jet1Hist6,Jet1Hist7,Jet1Hist8,Jet1Hist9,Jet1Hist10] #only put the hists you need
    Jet2HistArray = [Jet2Hist1,Jet2Hist2,Jet2Hist3,Jet2Hist4,Jet2Hist5,Jet2Hist6,Jet2Hist7,Jet2Hist8,Jet2Hist9,Jet2Hist10] #only put the hists you need
    Jet3HistArray = [Jet3Hist1,Jet3Hist2,Jet3Hist3,Jet3Hist4,Jet3Hist5,Jet3Hist6,Jet3Hist7,Jet3Hist8,Jet3Hist9,Jet3Hist10] #only put the hists you need
    TitlesArray = ["All Mjj [GeV] values","250 < Mjj [GeV] < 350","350 < Mjj [GeV] < 500","500 < Mjj [GeV] < 650","650 < Mjj [GeV] < 850","850 < Mjj [GeV] < 1100","1100 < Mjj [GeV] < 1400","1400 < Mjj [GeV] < 1800","1800 < Mjj [GeV] < 2200","2200 < Mjj [GeV]"]
    #add setLogy to function as last parameter when scale should be logy
    RootHisttoPdf(outDirectory+variable+"hists.pdf",Jet1HistArray,Jet2HistArray,Jet3HistArray,TitlesArray,xAxis,"N",histNum,setLogy)

def RootHisttoPdfGeneral(outFileName,data,titlesArray,xAxisTitle,yAxisTitle,histNum,logyScale):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data[0],"data")

    canvas.Print(outFileName+"[")
    for i in range(0,histNum):
        data[i].SetStats(0)
        data[i].SetLineColor(ROOT.kBlack)
        data[i].SetLineWidth(2)
        data[i].GetYaxis().SetTitle(yAxisTitle)
        data[i].GetXaxis().SetTitle(xAxisTitle)
        data[i].SetTitle("")
        data[i].Draw("pe")
        legend.Draw("same")
        latex.DrawText(0.5,0.8,titlesArray[i])
        canvas.Print(outFileName)
    canvas.Print(outFileName+"]")

def loadAndSaveGeneral(inDirectory,outDirectory,histNum,variable,xAxis,setLogy=False):
    Hist1,Hist2,Hist3,Hist4,Hist5,Hist6,Hist7,Hist8,Hist9,Hist10 = loadRootFiles(inDirectory+variable+"hists.root",variable+"allmjjvaluesHist",variable+"250to350Hist",variable+"350to500Hist",variable+"500to650Hist",variable+"650to850Hist",variable+"850to1100Hist",variable+"1100to1400Hist",variable+"1400to1800Hist",variable+"1800to2200Hist",variable+"over2200Hist")
    HistArray = [Hist1,Hist2,Hist3,Hist4,Hist5,Hist6,Hist7,Hist8,Hist9,Hist10] #only put the hists you need
    TitlesArray = ["All Mjj [GeV] values","250 < Mjj [GeV] < 350","350 < Mjj [GeV] < 500","500 < Mjj [GeV] < 650","650 < Mjj [GeV] < 850","850 < Mjj [GeV] < 1100","1100 < Mjj [GeV] < 1400","1400 < Mjj [GeV] < 1800","1800 < Mjj [GeV] < 2200","2200 < Mjj [GeV]"]
    #add setLogy to function as last parameter when scale should be logy
    RootHisttoPdfGeneral(outDirectory+variable+"hists.pdf",HistArray,TitlesArray,xAxis,"N",histNum,setLogy)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/DataFiles/Results/Roots/angularkinematics2023B/"
outDirectory = "/home/jmuecke/code/mueckejonas/DataFiles/Results/Pdfs/angularkinematics2023B/"

#create Jet pdfs
loadAndSave(inDirectory,outDirectory,10,"pt","Pt [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"eta","Eta")
loadAndSave(inDirectory,outDirectory,10,"y","Y")
loadAndSave(inDirectory,outDirectory,10,"m","Mass [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"phi","Phi")
loadAndSave(inDirectory,outDirectory,10,"jec","Jet energy correction ")
loadAndSave(inDirectory,outDirectory,10,"muf","Muon energy fraction ")
loadAndSave(inDirectory,outDirectory,10,"chf","Charged energy fraction ")
loadAndSave(inDirectory,outDirectory,10,"nhf","Charged energy fraction ")
loadAndSave(inDirectory,outDirectory,10,"area","Jet catchement area ")
loadAndSave(inDirectory,outDirectory,10,"nemf","Neutral em energy fraction ")
loadAndSave(inDirectory,outDirectory,10,"cemf","Charged em energy fraction ")
loadAndSave(inDirectory,outDirectory,10,"btagDeepFlavB","DeepJet b+bb+lepb tag discriminator ")
loadAndSave(inDirectory,outDirectory,10,"nConstituents","Particles in jet")
#create general pdfs
loadAndSaveGeneral(inDirectory,outDirectory,10,"yboost","Yboost")
loadAndSaveGeneral(inDirectory,outDirectory,10,"chi","Chi")
#create mjj pdf
mjjHist1,mjjHist2,mjjHist3,mjjHist4,mjjHist5,mjjHist6,mjjHist7,mjjHist8,mjjHist9,mjjHist10 = loadRootFiles(inDirectory+"mjjhists.root","mjj hist")
mjjHistArray = [mjjHist1] #only put the hists you need
mjjTitlesArray = ["All Mjj [GeV] values"]
histNum = 1 #put number of mjjHistArray length
#add setLogy to function as last parameter when scale should be logy
RootHisttoPdfGeneral(outDirectory+"mjjhists.pdf",mjjHistArray,mjjTitlesArray,"Mjj [GeV]","N",histNum,True)
