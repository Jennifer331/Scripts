function [] = plot_distance(file, label)
    load(file);
    matls = ["空瓶" "油" "醋" "水"];
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
        legend('RSSI距离', '相位距离', 'RSSI相关系数')
        ylabel('相关系数', 'FontSize', 30)
        yyaxis left
        ylabel('距离', 'FontSize', 30)
        xlabel('位置', 'FontSize', 30)
        title(matls(i))
%         set(gcf, 'PaperSize', [18 12]);
%         saveas(gcf, sprintf('%s_%s.pdf', label, matls(i)))
end

