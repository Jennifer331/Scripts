channel_list=unique(cha_w_90);
distance_list=unique(dis_w_90);
%% 水
cha_w=CHANNEL;
dis_w=DISTANCE;
phase_w=PHASE;
rssi_w=RSSI;

logica=dis_w<90;
cha_w_90=cha_w(logica);
dis_w_90=dis_w(logica);
phase_w_90=phase_w(logica);
rssi_w_90=rssi_w(logica);
%% 水_平板拟合
fitmod_rssi_w_90=fittedmodel2;
fitmod_phase_w_90=fittedmodel3;

[X,Y]=meshgrid(distance_list,channel_list);
fitdata_rssi_w_90=fitmod_rssi_w_90(X,Y);
fitdata_phase_w_90=fitmod_phase_w_90(X,Y);

%%
plot(fitdata_phase_w_90(:))
hold on
plot(fitdata_phase_v_90(:))

corrcoef(fitdata_phase_w_90(:),fitdata_phase_v_90(:))