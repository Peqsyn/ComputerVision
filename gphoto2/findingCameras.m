% Read CSV file
filename = 'Updated gphoto2 list.xlsx';
sheet = 'Sheet1';
% data = csvread(filename);
[blank, table] = xlsread(filename, sheet);

% finds the row to delete
removeCell = strcmp(table(:,3), ('Testing (Beta)  '));
table(removeCell,:)=[];

removeCell = strcmp(table(:,3), ('Deprecated  '));
table(removeCell,:)=[];

removeCell = strcmp(table(:,3), ('Experimental  '));
table(removeCell,:)=[];

newfilename = 'New New gphoto2 list.xlsx';
xlswrite(newfilename, table);