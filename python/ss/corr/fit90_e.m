%% ¿ÕÆ¿
cha_e=CHANNEL;
dis_e=DISTANCE;
phase_e=PHASE;
rssi_e=RSSI;

logica=dis_e<88;
cha_e_90=cha_e(logica);
dis_e_90=dis_e(logica);
phase_e_90=phase_e(logica);
rssi_e_90=rssi_e(logica);
%% ¿ÕÆ¿_Æ½°åÄâºÏ
fitmod_rssi_e_90=fittedmodel6;
fitmod_phase_e_90=fittedmodel7;

[X,Y]=meshgrid(distance_list,channel_list);
fitdata_rssi_e_90=fitmod_rssi_e_90(X,Y);
fitdata_phase_e_90=fitmod_phase_e_90(X,Y);