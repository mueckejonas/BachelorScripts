int PlotData()
{
  char rootFile[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char outNameJet1[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/Jet1.root";
  char outNameJet2[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/Jet2.root";
  char outNameJet3[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/Jet3.root";
  TFile* inFile = TFile::Open(rootFile,"READ");
  TTree* tree = (TTree*)inFile->Get("Events");

  const unsigned int eventNum = 1;
  float pt1Num[eventNum];
  float y1Num[eventNum];
  float eta1Num[eventNum];
  float phi1Num[eventNum];
  float mass1Num[eventNum];
  float jec1Num[eventNum];
  float muf1Num[eventNum];
  float nhf1Num[eventNum];
  float chf1Num[eventNum];
  float area1Num[eventNum];
  float nemf1Num[eventNum];
  float cemf1Num[eventNum];
  float btagDeepFlavB1Num[eventNum];
  float nConstituents1Num[eventNum];

  tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree->SetBranchAddress("jetAK4_y1",&y1Num);
  tree->SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree->SetBranchAddress("jetAK4_phi1",&phi1Num);
  tree->SetBranchAddress("jetAK4_mass1",&mass1Num);
  tree->SetBranchAddress("jetAK4_jec1",&jec1Num);
  tree->SetBranchAddress("jetAK4_muf1",&muf1Num);
  tree->SetBranchAddress("jetAK4_nhf1",&nhf1Num);
  tree->SetBranchAddress("jetAK4_chf1",&chf1Num);
  tree->SetBranchAddress("jetAK4_area1",&area1Num);
  tree->SetBranchAddress("jetAK4_nemf1",&nemf1Num);
  tree->SetBranchAddress("jetAK4_cemf1",&cemf1Num);
  tree->SetBranchAddress("jetAK4_btagDeepFlavB1",&btagDeepFlavB1Num);
  tree->SetBranchAddress("jetAK4_nConstituents1",&nConstituents1Num);

  TH1D pt1("datapt1","pt for jet1 data",50,0,1000);
  pt1.Sumw2();
  TH1D y1("datay1","y for jet1 data",50,-6,6);
  y1.Sumw2();
  TH1D eta1("dataeta1","eta for jet1 data",50,-6,6);
  eta1.Sumw2();
  TH1D phi1("dataphi1","phi for jet1 data",50,-4,4);
  phi1.Sumw2();
  TH1D mass1("datamass1","mass for jet1 data",50,0,200);
  mass1.Sumw2();
  TH1D jec1("datajec1","jec for jet1 data",50,0.5,1.3);
  jec1.Sumw2();
  TH1D muf1("datamuf1","muf for jet1 data",50,0,0.15);
  muf1.Sumw2();
  TH1D nhf1("datanhf1","nhf for jet1 data",50,0,0.4);
  nhf1.Sumw2();
  TH1D chf1("datachf1","chf for jet1 data",50,0,1);
  chf1.Sumw2();
  TH1D area1("dataarea1","area for jet1 data",50,0.2,0.8);
  area1.Sumw2();
  TH1D nemf1("datanemf1","nemf for jet1 data",50,0,1);
  nemf1.Sumw2();
  TH1D cemf1("datacemf1","cemf for jet1 data",50,0,0.15);
  cemf1.Sumw2();
  TH1D btagDeepFlavB1("databtagDeepFlavB1","btagDeepFlavB for jet1 data",50,0,1);
  btagDeepFlavB1.Sumw2();
  TH1D nConstituents1("datanConstituents1","nConstituents for jet1 data",50,0,100);
  nConstituents1.Sumw2();

  for (Long64_t entry = 0; entry < tree->GetEntries(); ++entry)
  {
    tree->GetEntry(entry);
    pt1.Fill(pt1Num[0]);
    y1.Fill(y1Num[0]);
    eta1.Fill(eta1Num[0]);
    phi1.Fill(phi1Num[0]);
    mass1.Fill(mass1Num[0]);
    jec1.Fill(jec1Num[0]);
    muf1.Fill(muf1Num[0]);
    nhf1.Fill(nhf1Num[0]);
    chf1.Fill(chf1Num[0]);
    area1.Fill(area1Num[0]);
    nemf1.Fill(nemf1Num[0]);
    cemf1.Fill(cemf1Num[0]);
    btagDeepFlavB1.Fill(btagDeepFlavB1Num[0]);
    nConstituents1.Fill(nConstituents1Num[0]);
  }

  pt1.SetDirectory(0);
  pt1.SetDirectory(0);
  y1.SetDirectory(0);
  eta1.SetDirectory(0);
  phi1.SetDirectory(0);
  mass1.SetDirectory(0);
  jec1.SetDirectory(0);
  muf1.SetDirectory(0);
  nhf1.SetDirectory(0);
  chf1.SetDirectory(0);
  area1.SetDirectory(0);
  nemf1.SetDirectory(0);
  cemf1.SetDirectory(0);
  btagDeepFlavB1.SetDirectory(0);
  nConstituents1.SetDirectory(0);
  inFile->Close();

  TFile* outHistFile = TFile::Open(outNameJet1,"RECREATE");
  outHistFile->mkdir("Jet1Data");
  outHistFile->cd("Jet1Data");
  pt1.Write();
  y1.Write();
  eta1.Write();
  phi1.Write();
  mass1.Write();
  jec1.Write();
  muf1.Write();
  nhf1.Write();
  chf1.Write();
  area1.Write();
  nemf1.Write();
  cemf1.Write();
  btagDeepFlavB1.Write();
  nConstituents1.Write();
  outHistFile->Close();

  return 0;
}
