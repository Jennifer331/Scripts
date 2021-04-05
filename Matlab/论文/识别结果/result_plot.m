load('test.mat')
d = mydata;
d(d==0) = -10;
d(isnan(d)) = 150;
imagesc(d)
colormap([1 0 0; 0 0 1; 0 1 0; 1 1 1]);

grid on
set(gca, 'XTick', 0:160/4:160);
set(gca, 'YTick', 0:160/4:160);

yticklabels({})
xticklabels({})