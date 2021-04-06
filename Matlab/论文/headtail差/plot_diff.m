% load('heatail_diff.mat')

%% ��λ
plot(e_p, 'x')
hold on
plot(o_p, 'x')
plot(v_p, 'x')
plot(w_p, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('��λ��/��rad��')
xticklabels({})
legend('��ƿ', '��', '��', 'ˮ')

%% RSSI
plot(e_r, 'x')
hold on
plot(o_r, 'x')
plot(v_r, 'x')
plot(w_r, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('�����ź�ǿ�Ȳ�/��dB��')
xticklabels({})
legend('��ƿ', '��', '��', 'ˮ')