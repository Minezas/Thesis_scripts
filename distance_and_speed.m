% Calcula da distancia total percorrida e velocidade média
% Unidade de calculo = pixel

% NOTA: os ficheiros de dados não podem conter headers!!

clear all

resol = 15; % frames por segundo

[file_name, filepath1] = uigetfile({'*.txt'}, 'Select TXT data file...');
    cd(filepath1);
	    data = load(file_name);
            data_length = length(data);
    
% Calculos            
    diff_xy = diff(data).^2;
    diff_xy_sum = sum(diff(data).^2,2);
    sequentialDistances = sqrt(sum(diff(data).^2,2));

    total_distance = sum(sequentialDistances);
        resol_sec = data_length/resol;
    mean_velocity = total_distance/resol_sec;
    
    disp('Total distance (pixels): ')
        total_distance
    disp('Mean velocity (pixel/sec): ')
        mean_velocity

% Print tracking vector
hold on
    plot(data(:,1),data(:,2)); title('Tracking vector'); ylabel('posY(px)'); xlabel('posX(px)')
hold off