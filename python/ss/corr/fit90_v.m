channel_list=unique(cha_v_90);
distance_list=unique(dis_v_90);
%% ´×
cha_v=CHANNEL;
dis_v=DISTANCE;
phase_v=PHASE;
rssi_v=RSSI;

logica=dis_v<90;
cha_v_90=cha_v(logica);
dis_v_90=dis_v(logica);
phase_v_90=phase_v(logica);
rssi_v_90=rssi_v(logica);
%% ´×_Æ½°åÄâºÏ
fitmod_rssi_v_90=fittedmodel;
fitmod_phase_v_90=fittedmodel1;

[X,Y]=meshgrid(distance_list,channel_list);
fitdata_rssi_v_90=fitmod_rssi_v_90(X,Y);
fitdata_phase_v_90=fitmod_phase_v_90(X,Y);

%%