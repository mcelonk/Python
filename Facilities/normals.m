format long g


XYZ = importdata('test_15k_bez_duplict.xyz');
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
quiver3(x,y,z,u,v,w);
hold off

S = [XYZ normaly];
writematrix(normaly, 'Normaly.txt','Delimiter','tab')
system('Facilities.py')