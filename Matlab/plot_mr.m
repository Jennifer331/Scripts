liquids = ["empty", "water", "ant_water", "p_water", "water2", "vinegar", "oil"];
markers = ['mp', 'k.', 'co', 'r*', 'gs', 'b+', 'yx'];
folder = "d:\\Atom\\python\\data\\cleaned\\mr";
file_kde = "mr_%s_kde.mat";
file_unwrap = "mr_%s_2d_unwrap_cus.mat";

folder2 = "d:\\Atom\\python\\data\\cleaned";
file2 = "nongfu_%s.mat";
liquids2 = ["empty", "oil", "water", "vinegar"];

waters = ["water", "ant_water", "p_water", "water2"];

liquids_contrast = ["water", "ant_water", "p_water", "water2", "vinegar", "oil", "empty"];
markers_contrast = ['m.', 'k.', 'b.', 'r.', 'gs', 'c+', 'yx'];

% plot_sa(folder, file_unwrap, liquids_contrast, markers_contrast)

folders = ["d:\\Atom\\python\\data\\cleaned", "d:\\Atom\\python\\data\\cleaned\\mr"];
patterns = ["nongfu_%s_2d_unwrap.mat", "mr_%s_2d_unwrap_cus.mat"];
liquids = ["empty", "water", "vinegar", "oil"];
markers = ["mo", "ko", "m*", "k*", "ms", "ks", "mx", "kx"];
plot_diff_folder(folders, patterns, liquids, markers)