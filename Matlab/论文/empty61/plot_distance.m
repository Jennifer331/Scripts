function [] = plot_distance(file, label)
    load(file);
    matls = ["��ƿ" "��" "��" "ˮ"];
    for i = 1:4
        figure(i)
        yyaxis left
        plot(d_r(i,:))
        hold on
        plot(d_p(i,:))
        yyaxis right
        plot(corr(i,:))
        legend('RSSI����', '��λ����', 'RSSI���ϵ��')
        ylabel('���ϵ��')
        yyaxis left
        ylabel('����')
        xlabel('λ��')
        title(matls(i))
        set(gcf, 'PaperSize', [18 12]);
        saveas(gcf, sprintf('%s_%s.pdf', label, matls(i)))
end

