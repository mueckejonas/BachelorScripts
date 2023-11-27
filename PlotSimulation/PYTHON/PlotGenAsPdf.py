import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,title,data2=None,data3=None,dataName="generated Jet1"):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1,dataName)
    if dataNumber > 2:
        legend.AddEntry(data2,"generated Jet2")
        legend.AddEntry(data3,"generated Jet3")
    else:
        legend.SetTextSize(0.03)

    data1.SetStats(0)
    data1.SetLineColor(ROOT.kBlack)
    data1.SetLineWidth(2)
    if dataNumber > 2:
        data2.SetStats(0)
        data2.SetLineColor(ROOT.kBlue)
        data2.SetLineWidth(2)
        data3.SetStats(0)
        data3.SetLineColor(ROOT.kRed)
        data3.SetLineWidth(2)
        data2.SetTitle("")
        data3.SetTitle("")
    data1.GetYaxis().SetTitle(yAxisTitle)
    data1.GetXaxis().SetTitle(xAxisTitle)
    data1.SetTitle("")
    data1.Draw("pe")
    if dataNumber > 2:
        data2.Draw("pe,same")
        data3.Draw("pe,same")
    legend.Draw("same")
    latex.DrawText(0.7,0.8,title)
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/PDF/Generation/"
inFileName = inDirectory+"Run32023_Gen.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
genJet1 = histFile.Get("genJet1")
genJet2 = histFile.Get("genJet2")
genJet3 = histFile.Get("genJet3")
Kinematics = histFile.Get("genKinematics")

genJetNameArray = np.array(["pt","y","eta","phi","mass"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]"])

#create Jet pdfs
for i in range(0,5):
    gen1 = genJet1.Get("gen"+genJetNameArray[i]+"1")
    gen2 = genJet2.Get("gen"+genJetNameArray[i]+"2")
    gen3 = genJet3.Get("gen"+genJetNameArray[i]+"3")

    if genJetNameArray[i] == "pt" or genJetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+"gen"+genJetNameArray[i]+".pdf",gen1,True,3,"N",XaxisArray[i],XaxisArray[i]+" generated",gen2,gen3)
    else:
        RootHisttoPdf(outDirectory+"gen"+genJetNameArray[i]+".pdf",gen1,False,3,"N",XaxisArray[i],XaxisArray[i]+" generated",gen2,gen3)

#create yboost pdf
yboostData = Kinematics.Get("Genyboost")
RootHisttoPdf(outDirectory+"gen"+"yboost.pdf",yboostData,False,1,"N","Yboost","Yboost generated","generated Yboost")
#create chi pdf
chiData = Kinematics.Get("Genchi")
RootHisttoPdf(outDirectory+"gen"+"chi.pdf",chiData,False,1,"N","Chi","Chi generated",None,None,"generated Chi")
#create mjj pdf
mjjData = Kinematics.Get("Genmjj")
RootHisttoPdf(outDirectory+"gen"+"mjj.pdf",mjjData,True,1,"N","Mjj [GeV]","Mjj generated",None,None,"generated Mjj")
