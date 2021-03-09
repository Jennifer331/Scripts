%% ”Õ
cha_o=CHANNEL;
dis_o=DISTANCE;
phase_o=PHASE;
rssi_o=RSSI;

logica=dis_o<90;
cha_o_90=cha_o(logica);
dis_o_90=dis_o(logica);
phase_o_90=phase_o(logica);
rssi_o_90=rssi_o(logica);
%% ”Õ_∆Ω∞Âƒ‚∫œ
fitmod_rssi_o_90=fittedmodel4;
fitmod_phase_o_90=fittedmodel5;

[X,Y]=meshgrid(distance_list,channel_list);
fitdata_rssi_o_90=fitmod_rssi_o_90(X,Y);
fitdata_phase_o_90=fitmod_phase_o_90(X,Y);