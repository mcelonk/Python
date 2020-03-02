format long g


XYZ = importdata('test_15k_bez_duplict.xyz'); % input, mus� b�t toto�n� jako v python scriptu
ptCloud = pointCloud(XYZ);
normaly = pcnormals(ptCloud); % v�po�et norm�ly pro ka�d� bod, ze 6 okoln�ch
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
quiver3(x,y,z,u,v,w); % vykreslen� norm�l
hold off

S = [XYZ normaly]; % kontroln� p�id�n� norm�l k jednotliv�m bod�m
writematrix(normaly, 'Normaly.txt','Delimiter','tab') % vytvo�en� matice
system('Facilities.py') % spu�t�n� python scriptu