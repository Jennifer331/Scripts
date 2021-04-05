function [] = plot_distance(file, label)
    load(file);
    matls = ["空瓶" "油" "醋" "水"];
    for i = 1:4
        figure(i)
        yyaxis left
        plot(d_r(i,:))
        hold on
        plot(d_p(i,:))
        yyaxis right
        plot(corr(i,:))
        legend('RSSI距离', '相位距离', 'RSSI相关系数')
        ylabel('相关系数')
        yyaxis left
        ylabel('距离')
        xlabel('位置')
        title(matls(i))
        set(gcf, 'PaperSize', [18 12]);
        saveas(gcf, sprintf('%s_%s.pdf', label, matls(i)))
end

