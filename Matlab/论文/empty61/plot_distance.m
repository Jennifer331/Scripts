function [] = plot_distance(file, label)
    load(file);
    matls = ["��ƿ" "��" "��" "ˮ"];
    for i = 1:3
        figure(i)
        set(gca, 'FontSize', 20)
        yyaxis left
        plot(d_r(i,:))
        hold on
        plot(d_p(i,:),'LineWidth', 2.0)
        yyaxis right
        plot(corr(i,:),'.-', 'MarkerSize', 15)
        hold off
        legend('RSSI����', '��λ����', 'RSSI���ϵ��')
        ylabel('���ϵ��', 'FontSize', 30)
        yyaxis left
        ylabel('����', 'FontSize', 30)
        xlabel('λ��', 'FontSize', 30)
        title(matls(i))
%         set(gcf, 'PaperSize', [18 12]);
%         saveas(gcf, sprintf('%s_%s.pdf', label, matls(i)))
end

