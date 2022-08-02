function varargout = appdetect(varargin)
% APPDETECT MATLAB code for appdetect.fig
%      APPDETECT, by itself, creates a new APPDETECT or raises the existing
%      singleton*.
%
%      H = APPDETECT returns the handle to a new APPDETECT or the handle to
%      the existing singleton*.
%
%      APPDETECT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in APPDETECT.M with the given input arguments.
%
%      APPDETECT('Property','Value',...) creates a new APPDETECT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before appdetect_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to appdetect_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help appdetect

% Last Modified by GUIDE v2.5 26-Dec-2021 14:24:23

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @appdetect_OpeningFcn, ...
                   'gui_OutputFcn',  @appdetect_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before appdetect is made visible.
function appdetect_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to appdetect (see VARARGIN)

% Choose default command line output for appdetect
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
ah = axes('unit','normalized','position',[0 0 1 1]);
bg = imread('bg.png');
imagesc(bg);
set(ah,'handlevisibility','off','visible','off')




% --- Outputs from this function are returned to the command line.
function varargout = appdetect_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in load_img.
function load_img_Callback(hObject, eventdata, handles)
% hObject    handle to load_img (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global im im2
[path,user_cancel] = imgetfile();
if user_cancel
    msgbox(sprintf('votre choix et invalide'),'Error','Warn');
    return
end
im =imread(path);
im = im2double(im);
im2 = im;
axes(handles.axes1);
imshow(im);
title(' Original Image');
   



% --- Executes on button press in detect.
function detect_Callback(hObject, eventdata, handles)
% hObject    handle to detect (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global im
axes(handles.axes2);
bw=im2bw(im,0.7);
label=bwlabel(bw);
stats=regionprops(label,'Solidity','Area');
density=[stats.Solidity];
area=[stats.Area];
high_dense_area=density>0.5;
max_area=max(area(high_dense_area));
tumor_label=find(area==max_area);
tumor=ismember(label,tumor_label);
se=strel('square',5);
tumor=imdilate(tumor,se);


[B]=bwboundaries(tumor,'noholes');

imshow(im);
hold on
for i=1:length(B)
    plot(B{i}(:,2),B{i}(:,1), 'y' ,'linewidth',1.45);
end
title('Cancer Detecte');
hold off


% --------------------------------------------------------------------
function about_Callback(hObject, eventdata, handles)
% hObject    handle to about (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function auteur_Callback(hObject, eventdata, handles)
% hObject    handle to auteur (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
msgbox(sprintf('coded by : Boulbalah Lahcen  '),'Auteur','Help');


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
