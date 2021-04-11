load('diff_test.mat')

%%
color = get(gca, 'ColorOrder');
m_open = 's';
m_out = 'x';
plot(open_empty_p, open_empty_r, m_open, 'color', color(1,:))
hold on
plot(open_oil_p, open_oil_r, m_open, 'color', color(2,:))
plot(open_vinegar_p, open_vinegar_r, m_open, 'color', color(3,:))
plot(open_water_p, open_water_r, m_open, 'color', color(4,:))

plot(outdoor_empty_p, outdoor_empty_r, m_out, 'color', color(1,:))
plot(outdoor_oil_p, outdoor_oil_r, m_out', 'color', color(2,:))
plot(outdoor_vinegar_p, outdoor_vinegar_r, m_out, 'color', color(3,:))
plot(outdoor_water_p, outdoor_water_r, m_out, 'color', color(4,:))

hold off
ylabel('��λ��/��rad��')
xlabel('�����ź�ǿ�Ȳ�/��dB��')
legend('����-��ƿ', '����-��', '����-��', '����-ˮ', '����-��ƿ', '����-��', '����-��', '����-ˮ')