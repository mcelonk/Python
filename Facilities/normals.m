format long g


XYZ = importdata('test_15k_bez_duplict.xyz'); % input, musí být totožný jako v python scriptu
ptCloud = pointCloud(XYZ);
normaly = pcnormals(ptCloud); % výpoèet normály pro každý bod, ze 6 okolních
ptCloud = pointCloud(XYZ,'Normal',normaly);

figure
pcshow(ptCloud)
title('Estimated Normals of Point Cloud')
hold on

x = ptCloud.Location(:,1);
y = ptCloud.Location(:,2);
z = ptCloud.Location(:,3);
u = normaly(:,1);
v = normaly(:,1);
w = normaly(:,1);
ptCloud
quiver3(x,y,z,u,v,w); % vykreslení normál
hold off

S = [XYZ normaly]; % kontrolní pøidání normál k jednotlivým bodùm
writematrix(normaly, 'Normaly.txt','Delimiter','tab') % vytvoøení matice
system('Facilities.py') % spuštìní python scriptu