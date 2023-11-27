int RootToHistSim()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
  char rootFile2[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
  char rootFile3[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
  char outName1[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/Run32023_MC.root";
  char outName2[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/Run32023_Gen.root";

   TChain tree("Events");   // name of the tree is the argument
   tree.Add(rootFile1);
   tree.Add(rootFile2);
   tree.Add(rootFile3);

  //declare variables to Load from Root Tree
  const unsigned int eventNum = 1;
  //variables of Jet1
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

  tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree.SetBranchAddress("jetAK4_y1",&y1Num);
  tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
  tree.SetBranchAddress("jetAK4_mass1",&mass1Num);
  tree.SetBranchAddress("jetAK4_jec1",&jec1Num);
  tree.SetBranchAddress("jetAK4_muf1",&muf1Num);
  tree.SetBranchAddress("jetAK4_nhf1",&nhf1Num);
  tree.SetBranchAddress("jetAK4_chf1",&chf1Num);
  tree.SetBranchAddress("jetAK4_area1",&area1Num);
  tree.SetBranchAddress("jetAK4_nemf1",&nemf1Num);
  tree.SetBranchAddress("jetAK4_cemf1",&cemf1Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB1",&btagDeepFlavB1Num);
  tree.SetBranchAddress("jetAK4_nConstituents1",&nConstituents1Num);

  TH1D pt1("MCpt1","pt for jet1 MC",50,0,4000);
  pt1.Sumw2();
  TH1D y1("MCy1","y for jet1 MC",50,-6,6);
  y1.Sumw2();
  TH1D eta1("MCeta1","eta for jet1 MC",50,-6,6);
  eta1.Sumw2();
  TH1D phi1("MCphi1","phi for jet1 MC",50,-4,4);
  phi1.Sumw2();
  TH1D mass1("MCmass1","mass for jet1 MC",50,0,300);
  mass1.Sumw2();
  TH1D jec1("MCjec1","jec for jet1 MC",50,0.5,1.3);
  jec1.Sumw2();
  TH1D muf1("MCmuf1","muf for jet1 MC",50,0,1);
  muf1.Sumw2();
  TH1D nhf1("MCnhf1","nhf for jet1 MC",50,0,1);
  nhf1.Sumw2();
  TH1D chf1("MCchf1","chf for jet1 MC",50,0,1);
  chf1.Sumw2();
  TH1D area1("MCarea1","area for jet1 MC",50,0.2,1);
  area1.Sumw2();
  TH1D nemf1("MCnemf1","nemf for jet1 MC",50,0,1);
  nemf1.Sumw2();
  TH1D cemf1("MCcemf1","cemf for jet1 MC",50,0,1);
  cemf1.Sumw2();
  TH1D btagDeepFlavB1("MCbtagDeepFlavB1","btagDeepFlavB for jet1 MC",50,0,1);
  btagDeepFlavB1.Sumw2();
  TH1D nConstituents1("MCnConstituents1","nConstituents for jet1 MC",50,0,100);
  nConstituents1.Sumw2();

  //variables of Jet2
  float pt2Num[eventNum];
  float y2Num[eventNum];
  float eta2Num[eventNum];
  float phi2Num[eventNum];
  float mass2Num[eventNum];
  float jec2Num[eventNum];
  float muf2Num[eventNum];
  float nhf2Num[eventNum];
  float chf2Num[eventNum];
  float area2Num[eventNum];
  float nemf2Num[eventNum];
  float cemf2Num[eventNum];
  float btagDeepFlavB2Num[eventNum];
  float nConstituents2Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
  tree.SetBranchAddress("jetAK4_y2",&y2Num);
  tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
  tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
  tree.SetBranchAddress("jetAK4_mass2",&mass2Num);
  tree.SetBranchAddress("jetAK4_jec2",&jec2Num);
  tree.SetBranchAddress("jetAK4_muf2",&muf2Num);
  tree.SetBranchAddress("jetAK4_nhf2",&nhf2Num);
  tree.SetBranchAddress("jetAK4_chf2",&chf2Num);
  tree.SetBranchAddress("jetAK4_area2",&area2Num);
  tree.SetBranchAddress("jetAK4_nemf2",&nemf2Num);
  tree.SetBranchAddress("jetAK4_cemf2",&cemf2Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB2",&btagDeepFlavB2Num);
  tree.SetBranchAddress("jetAK4_nConstituents2",&nConstituents2Num);

  TH1D pt2("MCpt2","pt for jet2 MC",50,0,4000);
  pt2.Sumw2();
  TH1D y2("MCy2","y for jet2 MC",50,-6,6);
  y2.Sumw2();
  TH1D eta2("MCeta2","eta for jet2 MC",50,-6,6);
  eta2.Sumw2();
  TH1D phi2("MCphi2","phi for jet2 MC",50,-4,4);
  phi2.Sumw2();
  TH1D mass2("MCmass2","mass for jet2 MC",50,0,300);
  mass2.Sumw2();
  TH1D jec2("MCjec2","jec for jet2 MC",50,0.5,1.3);
  jec2.Sumw2();
  TH1D muf2("MCmuf2","muf for jet2 MC",50,0,1);
  muf2.Sumw2();
  TH1D nhf2("MCnhf2","nhf for jet2 MC",50,0,1);
  nhf2.Sumw2();
  TH1D chf2("MCchf2","chf for jet2 MC",50,0,1);
  chf2.Sumw2();
  TH1D area2("MCarea2","area for jet2 MC",50,0.2,1);
  area2.Sumw2();
  TH1D nemf2("MCnemf2","nemf for jet2 MC",50,0,1);
  nemf2.Sumw2();
  TH1D cemf2("MCcemf2","cemf for jet2 MC",50,0,1);
  cemf2.Sumw2();
  TH1D btagDeepFlavB2("MCbtagDeepFlavB2","btagDeepFlavB for jet2 MC",50,0,1);
  btagDeepFlavB2.Sumw2();
  TH1D nConstituents2("MCnConstituents2","nConstituents for jet2 MC",50,0,100);
  nConstituents2.Sumw2();

  //variables of Jet3
  float pt3Num[eventNum];
  float y3Num[eventNum];
  float eta3Num[eventNum];
  float phi3Num[eventNum];
  float mass3Num[eventNum];
  float jec3Num[eventNum];
  float muf3Num[eventNum];
  float nhf3Num[eventNum];
  float chf3Num[eventNum];
  float area3Num[eventNum];
  float nemf3Num[eventNum];
  float cemf3Num[eventNum];
  float btagDeepFlavB3Num[eventNum];
  float nConstituents3Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
  tree.SetBranchAddress("jetAK4_y3",&y3Num);
  tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
  tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
  tree.SetBranchAddress("jetAK4_mass3",&mass3Num);
  tree.SetBranchAddress("jetAK4_jec3",&jec3Num);
  tree.SetBranchAddress("jetAK4_muf3",&muf3Num);
  tree.SetBranchAddress("jetAK4_nhf3",&nhf3Num);
  tree.SetBranchAddress("jetAK4_chf3",&chf3Num);
  tree.SetBranchAddress("jetAK4_area3",&area3Num);
  tree.SetBranchAddress("jetAK4_nemf3",&nemf3Num);
  tree.SetBranchAddress("jetAK4_cemf3",&cemf3Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB3",&btagDeepFlavB3Num);
  tree.SetBranchAddress("jetAK4_nConstituents3",&nConstituents3Num);

  TH1D pt3("MCpt3","pt for jet3 MC",50,0,4000);
  pt3.Sumw2();
  TH1D y3("MCy3","y for jet3 MC",50,-6,6);
  y3.Sumw2();
  TH1D eta3("MCeta3","eta for jet3 MC",50,-6,6);
  eta3.Sumw2();
  TH1D phi3("MCphi3","phi for jet3 MC",50,-4,4);
  phi3.Sumw2();
  TH1D mass3("MCmass3","mass for jet3 MC",50,0,200);
  mass3.Sumw2();
  TH1D jec3("MCjec3","jec for jet3 MC",50,0.5,1.3);
  jec3.Sumw2();
  TH1D muf3("MCmuf3","muf for jet3 MC",50,0,1);
  muf3.Sumw2();
  TH1D nhf3("MCnhf3","nhf for jet3 MC",50,0,1);
  nhf3.Sumw2();
  TH1D chf3("MCchf3","chf for jet3 MC",50,0,1);
  chf3.Sumw2();
  TH1D area3("MCarea3","area for jet3 MC",50,0.2,1);
  area3.Sumw2();
  TH1D nemf3("MCnemf3","nemf for jet3 MC",50,0,1);
  nemf3.Sumw2();
  TH1D cemf3("MCcemf3","cemf for jet3 MC",50,0,1);
  cemf3.Sumw2();
  TH1D btagDeepFlavB3("MCbtagDeepFlavB3","btagDeepFlavB for jet3 MC",50,0,1);
  btagDeepFlavB3.Sumw2();
  TH1D nConstituents3("MCnConstituents3","nConstituents for jet3 MC",50,0,100);
  nConstituents3.Sumw2();

  //Create quantities calculated from variables
  TH1D MjjHist("MCmjj","Mjj [Gev]",50,2000,8000);
  MjjHist.Sumw2();

  TH1D YBoostHist("MCyboost","YBoost",50,0,2);
  YBoostHist.Sumw2();

  TH1D ChiHist("MCchi","Chi",50,0,16);
  ChiHist.Sumw2();

  //variables of genJet
  float genpt1Num[eventNum];
  float geny1Num[eventNum];
  float geneta1Num[eventNum];
  float genphi1Num[eventNum];
  float genmass1Num[eventNum];
  float genpt2Num[eventNum];
  float geny2Num[eventNum];
  float geneta2Num[eventNum];
  float genphi2Num[eventNum];
  float genmass2Num[eventNum];
  float genpt3Num[eventNum];
  float geny3Num[eventNum];
  float geneta3Num[eventNum];
  float genphi3Num[eventNum];
  float genmass3Num[eventNum];

  tree.SetBranchAddress("genJetAK4_pt1",&genpt1Num);
  tree.SetBranchAddress("genJetAK4_y1",&geny1Num);
  tree.SetBranchAddress("genJetAK4_eta1",&geneta1Num);
  tree.SetBranchAddress("genJetAK4_phi1",&genphi1Num);
  tree.SetBranchAddress("genJetAK4_mass1",&genmass1Num);
  tree.SetBranchAddress("genJetAK4_pt2",&genpt2Num);
  tree.SetBranchAddress("genJetAK4_y2",&geny2Num);
  tree.SetBranchAddress("genJetAK4_eta2",&geneta2Num);
  tree.SetBranchAddress("genJetAK4_phi2",&genphi2Num);
  tree.SetBranchAddress("genJetAK4_mass2",&genmass2Num);
  tree.SetBranchAddress("genJetAK4_pt3",&genpt3Num);
  tree.SetBranchAddress("genJetAK4_y3",&geny3Num);
  tree.SetBranchAddress("genJetAK4_eta3",&geneta3Num);
  tree.SetBranchAddress("genJetAK4_phi3",&genphi3Num);
  tree.SetBranchAddress("genJetAK4_mass3",&genmass3Num);


  TH1D genpt1("genpt1","pt for genJet1",50,0,4000);
  genpt1.Sumw2();
  TH1D geny1("geny1","y for genJet1",50,-6,6);
  geny1.Sumw2();
  TH1D geneta1("geneta1","eta for genJet1",50,-6,6);
  geneta1.Sumw2();
  TH1D genphi1("genphi1","phi for genJet1",50,-4,4);
  genphi1.Sumw2();
  TH1D genmass1("genmass1","mass for genJet1",50,0,200);
  genmass1.Sumw2();
  TH1D genpt2("genpt2","pt for genJet2",50,0,4000);
  genpt2.Sumw2();
  TH1D geny2("geny2","y for genJet2",50,-6,6);
  geny2.Sumw2();
  TH1D geneta2("geneta2","eta for genJet2",50,-6,6);
  geneta2.Sumw2();
  TH1D genphi2("genphi2","phi for genJet2",50,-4,4);
  genphi2.Sumw2();
  TH1D genmass2("genmass2","mass for genJet2",50,0,200);
  genmass2.Sumw2();
  TH1D genpt3("genpt3","pt for genJet3",50,0,4000);
  genpt3.Sumw2();
  TH1D geny3("geny3","y for genJet3",50,-6,6);
  geny3.Sumw2();
  TH1D geneta3("geneta3","eta for genJet3",50,-6,6);
  geneta3.Sumw2();
  TH1D genphi3("genphi3","phi for genJet3",50,-4,4);
  genphi3.Sumw2();
  TH1D genmass3("genmass3","mass for genJet3",50,0,200);
  genmass3.Sumw2();

  //caulculate qunatities from variables of gen jets
  TH1D genMjjHist("Genmjj","Mjj [Gev]",50,2000,8000);
  genMjjHist.Sumw2();

  TH1D genYBoostHist("Genyboost","YBoost",50,0,2);
  genYBoostHist.Sumw2();

  TH1D genChiHist("Genchi","Chi",50,0,16);
  genChiHist.Sumw2();


  //Fill the Hists with Root Tree MC and Genjets
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);

    //Calculate MC Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
    Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();

    //Calculate MC chi
    double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

    //Calculate MC yboost
    double YBoostValue = (y1Num[0]+y2Num[0])/2;

    if (MjjValue > 0 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      //Fill mcJet1
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

      //Fill mcJet2
      pt2.Fill(pt2Num[0]);
      y2.Fill(y2Num[0]);
      eta2.Fill(eta2Num[0]);
      phi2.Fill(phi2Num[0]);
      mass2.Fill(mass2Num[0]);
      jec2.Fill(jec2Num[0]);
      muf2.Fill(muf2Num[0]);
      nhf2.Fill(nhf2Num[0]);
      chf2.Fill(chf2Num[0]);
      area2.Fill(area2Num[0]);
      nemf2.Fill(nemf2Num[0]);
      cemf2.Fill(cemf2Num[0]);
      btagDeepFlavB2.Fill(btagDeepFlavB2Num[0]);
      nConstituents2.Fill(nConstituents2Num[0]);

      //Fill mcJet3
      pt3.Fill(pt3Num[0]);
      y3.Fill(y3Num[0]);
      eta3.Fill(eta3Num[0]);
      phi3.Fill(phi3Num[0]);
      mass3.Fill(mass3Num[0]);
      jec3.Fill(jec3Num[0]);
      muf3.Fill(muf3Num[0]);
      nhf3.Fill(nhf3Num[0]);
      chf3.Fill(chf3Num[0]);
      area3.Fill(area3Num[0]);
      nemf3.Fill(nemf3Num[0]);
      cemf3.Fill(cemf3Num[0]);
      btagDeepFlavB3.Fill(btagDeepFlavB3Num[0]);
      nConstituents3.Fill(nConstituents3Num[0]);

      //fill MCyboost
      YBoostHist.Fill(YBoostValue);

      //fill MCMjj
      MjjHist.Fill(MjjValue);

      //fill MCchi
      ChiHist.Fill(ChiValue);
    }

    //Calculate Mjj
    TLorentzVector genLorentz0, genLorentz1;
    genLorentz0.SetPtEtaPhiM(genpt1Num[0],geneta1Num[0],genphi1Num[0],genmass1Num[0]);
    genLorentz1.SetPtEtaPhiM(genpt2Num[0],geneta2Num[0],genphi2Num[0],genmass2Num[0]);
    TLorentzVector genMjjSum = genLorentz0 + genLorentz1;
    double genMjjValue = genMjjSum.M();

    //Calculate chi
    double genChiValue = exp(abs(geny1Num[0]-geny2Num[0]));

    //Calculate yboost
    double genYBoostValue = (geny1Num[0]+geny2Num[0])/2;

    if (genMjjValue > 0 && genChiValue < 16 && abs(genYBoostValue) < 1.11)
    {
      //Fill genJet1
      genpt1.Fill(genpt1Num[0]);
      geny1.Fill(geny1Num[0]);
      geneta1.Fill(geneta1Num[0]);
      genphi1.Fill(genphi1Num[0]);
      genmass1.Fill(genmass1Num[0]);
      //Fill genJet2
      genpt2.Fill(genpt2Num[0]);
      geny2.Fill(geny2Num[0]);
      geneta2.Fill(geneta2Num[0]);
      genphi2.Fill(genphi2Num[0]);
      genmass2.Fill(genmass2Num[0]);
      //Fill genJet3
      genpt3.Fill(genpt3Num[0]);
      geny3.Fill(geny3Num[0]);
      geneta3.Fill(geneta3Num[0]);
      genphi3.Fill(genphi3Num[0]);
      genmass3.Fill(genmass3Num[0]);

      //Fill genmjj
      genMjjHist.Fill(genMjjValue);
      //fill genchi
      genChiHist.Fill(genChiValue);
      //fill genyboost
      genYBoostHist.Fill(genYBoostValue);
    }
  }

  //Neccesary so files dont get lost
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
  pt2.SetDirectory(0);
  pt2.SetDirectory(0);
  y2.SetDirectory(0);
  eta2.SetDirectory(0);
  phi2.SetDirectory(0);
  mass2.SetDirectory(0);
  jec2.SetDirectory(0);
  muf2.SetDirectory(0);
  nhf2.SetDirectory(0);
  chf2.SetDirectory(0);
  area2.SetDirectory(0);
  nemf2.SetDirectory(0);
  cemf2.SetDirectory(0);
  btagDeepFlavB2.SetDirectory(0);
  nConstituents2.SetDirectory(0);
  pt3.SetDirectory(0);
  pt3.SetDirectory(0);
  y3.SetDirectory(0);
  eta3.SetDirectory(0);
  phi3.SetDirectory(0);
  mass3.SetDirectory(0);
  jec3.SetDirectory(0);
  muf3.SetDirectory(0);
  nhf3.SetDirectory(0);
  chf3.SetDirectory(0);
  area3.SetDirectory(0);
  nemf3.SetDirectory(0);
  cemf3.SetDirectory(0);
  btagDeepFlavB3.SetDirectory(0);
  nConstituents3.SetDirectory(0);
  MjjHist.SetDirectory(0);
  YBoostHist.SetDirectory(0);
  ChiHist.SetDirectory(0);
  genpt1.SetDirectory(0);
  genpt1.SetDirectory(0);
  geny1.SetDirectory(0);
  geneta1.SetDirectory(0);
  genphi1.SetDirectory(0);
  genmass1.SetDirectory(0);
  genpt2.SetDirectory(0);
  genpt2.SetDirectory(0);
  geny2.SetDirectory(0);
  geneta2.SetDirectory(0);
  genphi2.SetDirectory(0);
  genmass2.SetDirectory(0);
  genpt3.SetDirectory(0);
  genpt3.SetDirectory(0);
  geny3.SetDirectory(0);
  geneta3.SetDirectory(0);
  genphi3.SetDirectory(0);
  genmass3.SetDirectory(0);
  genMjjHist.SetDirectory(0);
  genYBoostHist.SetDirectory(0);
  genChiHist.SetDirectory(0);


  TFile* outHistFile1 = TFile::Open(outName1,"RECREATE");
  //Write Jet1 MC to Root
  outHistFile1->mkdir("Jet1MC");
  outHistFile1->cd("Jet1MC");
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
  //Write Jet2 MC to Root
  outHistFile1->mkdir("Jet2MC");
  outHistFile1->cd("Jet2MC");
  pt2.Write();
  y2.Write();
  eta2.Write();
  phi2.Write();
  mass2.Write();
  jec2.Write();
  muf2.Write();
  nhf2.Write();
  chf2.Write();
  area2.Write();
  nemf2.Write();
  cemf2.Write();
  btagDeepFlavB2.Write();
  nConstituents2.Write();
  //Write Jet3 MC to Root
  outHistFile1->mkdir("Jet3MC");
  outHistFile1->cd("Jet3MC");
  pt3.Write();
  y3.Write();
  eta3.Write();
  phi3.Write();
  mass3.Write();
  jec3.Write();
  muf3.Write();
  nhf3.Write();
  chf3.Write();
  area3.Write();
  nemf3.Write();
  cemf3.Write();
  btagDeepFlavB3.Write();
  nConstituents3.Write();
  //Write quantities to Root
  outHistFile1->mkdir("MCKinematics");
  outHistFile1->cd("MCKinematics");
  MjjHist.Write();
  YBoostHist.Write();
  ChiHist.Write();
  outHistFile1->Close();

TFile* outHistFile2 = TFile::Open(outName2,"RECREATE");
  //Write genJet1 to Root
  outHistFile2->mkdir("genJet1");
  outHistFile2->cd("genJet1");
  genpt1.Write();
  geny1.Write();
  geneta1.Write();
  genphi1.Write();
  genmass1.Write();
  //Write genJet2 to Root
  outHistFile2->mkdir("genJet2");
  outHistFile2->cd("genJet2");
  genpt2.Write();
  geny2.Write();
  geneta2.Write();
  genphi2.Write();
  genmass2.Write();
  //Write genJet3 to Root
  outHistFile2->mkdir("genJet3");
  outHistFile2->cd("genJet3");
  genpt3.Write();
  geny3.Write();
  geneta3.Write();
  genphi3.Write();
  genmass3.Write();
  //Write genjet quantities to Root
  outHistFile2->mkdir("genKinematics");
  outHistFile2->cd("genKinematics");
  genMjjHist.Write();
  genYBoostHist.Write();
  genChiHist.Write();
  outHistFile2->Close();

  return 0;
}
