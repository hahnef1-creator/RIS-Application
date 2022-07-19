from kivy.resources import resource_add_path
from kivymd.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from kivy.config import Config
import sys
import os
Config.set('graphics','multisamples','0')
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
if getattr(sys, 'frozen', False):
    # this is a Pyinstaller bundle
    resource_add_path(sys._MEIPASS)
    resource_add_path(os.path.join(sys._MEIPASS, 'media'))


Config.set('input', 'mouse', 'mouse,disable_multitouch')

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 1)

town_lookup = {
 
    '001':'ANDOVER',
'002':'ANSONIA',
'003':'ASHFORD',
'004':'AVON',
'005':'BARKHAMSTED',
'006':'BEACON FALLS',
'007':'BERLIN',
'008':'BETHANY',
'009':'BETHEL',
'010':'BETHLEHEM',
'011':'BLOOMFIELD',
'012':'BOLTON',
'013':'BOZRAH',
'014':'BRANFORD',
'015':'BRIDGEPORT',
'016':'BRIDGEWATER',
'017':'BRISTOL',
'018':'BROOKFIELD',
'019':'BROOKLYN',
'020':'BURLINGTON',
'021':'CANAAN',
'022':'CANTERBURY',
'023':'CANTON',
'024':'CHAPLIN',
'025':'CHESHIRE',
'026':'CHESTER',
'027':'CLINTON',
'028':'COLCHESTER',
'029':'COLEBROOK',
'030':'COLUMBIA',
'031':'CORNWALL',
'032':'COVENTRY',
'033':'CROMWELL',
'034':'DANBURY',
'035':'DARIEN',
'036':'DERBY',
'037':'DURHAM',
'038':'EASTFORD',
'039':'EAST GRANBY',
'040':'EAST HADDAM',
'041':'EAST HAMPTON',
'042':'EAST HARTFORD',
'043':'EAST HAVEN',
'044':'EAST LYME',
'045':'EASTON',
'046':'EAST WINDSOR',
'047':'ELLINGTON',
'048':'ENFIELD',
'049':'ESSEX',
'050':'FAIRFIELD',
'051':'FARMINGTON',
'052':'FRANKLIN',
'053':'GLASTONBURY',
'054':'GOSHEN',
'055':'GRANBY',
'056':'GREENWICH',
'057':'GRISWOLD',
'058':'GROTON',
'059':'GUILFORD',
'060':'HADDAM',
'061':'HAMDEN',
'062':'HAMPTON',
'063':'HARTFORD',
'064':'HARTLAND',
'065':'HARWINTON',
'066':'HEBRON',
'067':'KENT',
'068':'KILLINGLY',
'069':'KILLINGWORTH',
'070':'LEBANON',
'071':'LEDYARD',
'072':'LISBON',
'073':'LITCHFIELD',
'074':'LYME',
'075':'MADISON',
'076':'MANCHESTER',
'077':'MANSFIELD',
'078':'MARLBOROUGH',
'079':'MERIDEN',
'080':'MIDDLEBURY',
'081':'MIDDLEFIELD',
'082':'MIDDLETOWN',
'083':'MILFORD',
'084':'MONROE',
'085':'MONTVILLE',
'086':'MORRIS',
'087':'NAUGATUCK',
'088':'NEW BRITAIN',
'089':'NEW CANAAN',
'090':'NEW FAIRFIELD',
'091':'NEW HARTFORD',
'092':'NEW HAVEN',
'093':'NEWINGTON',
'094':'NEW LONDON',
'095':'NEW MILFORD',
'096':'NEWTOWN',
'097':'NORFOLK',
'098':'NORTH BRANFORD',
'099':'NORTH CANAAN',
'100':'NORTH HAVEN',
'101':'NORTH STONINGTON',
'102':'NORWALK',
'103':'NORWICH',
'104':'OLD LYME',
'105':'OLD SAYBROOK',
'106':'ORANGE',
'107':'OXFORD',
'108':'PLAINFIELD',
'109':'PLAINVILLE',
'110':'PLYMOUTH',
'111':'POMFRET',
'112':'PORTLAND',
'113':'PRESTON',
'114':'PROSPECT',
'115':'PUTNAM',
'116':'REDDING',
'117':'RIDGEFIELD',
'118':'ROCKY HILL',
'119':'ROXBURY',
'120':'SALEM',
'121':'SALISBURY',
'122':'DEEP RIVER',
'123':'SCOTLAND',
'124':'SEYMOUR',
'125':'SHARON',
'126':'SHELTON',
'127':'SHERMAN',
'128':'SIMSBURY',
'129':'SOMERS',
'130':'SOUTHBURY',
'131':'SOUTHINGTON',
'132':'SOUTH WINDSOR',
'133':'SPRAGUE',
'134':'STAFFORD',
'135':'STAMFORD',
'136':'STERLING',
'137':'STONINGTON',
'138':'STRATFORD',
'139':'SUFFIELD',
'140':'THOMASTON',
'141':'THOMPSON',
'142':'TOLLAND',
'143':'TORRINGTON',
'144':'TRUMBULL',
'145':'UNION',
'146':'VERNON',
'147':'VOLUNTOWN',
'148':'WALLINGFORD',
'149':'WARREN',
'150':'WASHINGTON',
'151':'WATERBURY',
'152':'WATERFORD',
'153':'WATERTOWN',
'154':'WESTBROOK',
'155':'WEST HARTFORD',
'156':'WEST HAVEN',
'157':'WESTON',
'158':'WESTPORT',
'159':'WETHERSFIELD',
'160':'WILLINGTON',
'161':'WILTON',
'162':'WINCHESTER',
'163':'WINDHAM',
'164':'WINDSOR',
'165':'WINDSOR LOCKS',
'166':'WOLCOTT',
'167':'WOODBRIDGE',
'168':'WOODBURY',
'169':'WOODSTOCK'
}

road_type_lookup = {
  
"A":"ROUTES, SSR'S AND SR'S",
"B":"Federal Aid over local road",
"C":"State Maint., Stubs and By-passed Sections",
"E":"Ramps and TR's",
"F":"State Maint. Connectors",
"G":"Frontage Roads",
"H":"Built-closed to Traffic",
"I":"Proposed Federal Aid",
"J":"Proposed State System",
"K":"Off Line",
"L":"State Park",
"M":"State Forest",
"N":"State Institution",
"Z":"ADT Double Description Card"
}

road_class_lookup = {
   
'A':'Interstate',
'B':'U.S. Number',
'C':'State Route Number',
'D':'State Special Service Number',
'E':'State Road Number on State System',
'F':'State Route or Road Number not on State System (legislative)',
'G':'Locally Maint. Rds. Serving as part of a State Rt. Or Rd., on State System (municipal ext.)',
'H':'Overlap',
'I':'State Institution Road serving as part of a State Route or Road',
'J':'Proposed location shown in highway log',
'K':'State Maintained, identification number assigned,i.e.,989 C, D, E',
'L':'State maintained stubs and by-passed sections and HOV lanes',
'M':'Access Ramp (non-expressway to expressway)',
'N':'Exit Ramp (expressway to non-expressway)',
'O':'2 - direction ramp (access and exit)',
'P':'Turning Roadway (between 2 expressways)',
'Q':'Connector State Maintained (between 2 non-expressways)',
'R':'Proposed location not shown in highway log  FA',
'S':'Proposed location not shown in highway log  NFA',
'T':'"Locally maint. Rd., not part of a state Rt. or Road on State System"',
'U':'"Locally maint. Rd., not part of a state Rt. or Road on State System (Legis.)"',
'V':'Connector - locally maintained (between 2 non-expressways)',
'W':'State Agency Roads'
}

road_status_lookup = {
   
    '0':'No Data',
'A':'Existing (Open to Traffic)',
'B':'Built, not open to traffic',
'C':'Under Construction',
'D':'Under Planning Design',
'E':'Temporary construction or Routing',
'X':'No Status'
}

tiepoint_code_lookup = {
  
    '9000':'OTHER TIEPOINT',
'9800':'Speed Bump',
'9801':'END LANE DROP',
'9802':'BGN LANE DROP',
'9804':'INCIDENT MANAGEMENT SERVICE CABINET',
'9805':'END TURN AROUND',
'9806':'BGN TURN AROUND',
'9807':'LOOPS',
'9808':'INFRA-RED BEAM/RADAR DET',
'9809':'TRAFFIC COUNTER CABINET',
'9810':'TRAFFIC SENSOR',
'9811':'LOOP COUNTERS',
'9812':'BGN ONE-WAY ALTERNATING TRAFFIC',
'9813':'END ONE-WAY ALTERNATING TRAFFIC',
'9814':'ITS CAMERA LOCATION',
'9815':'WEATHER STATION',
'9816':'BGN MOVABLE BRIDGE',
'9817':'END MOVABLE BRIDGE',
'9818':'OVERHEAD VMS SIGN',
'9819':'FLASHING SIGN',
'9820':'TRAFFIC SIGNAL',
'9821':'WIM LOCATIONS',
'9822':'CLASSIFICATION COUNTERS',
'9823':'MIDBLOCK PEDESTRIAN X-ING',
'9824':'MIDBLOCK PED X-ING W/DEVICES',
'9825':'Abandoned RR crossing (Tracks not removed)',
'9826':'End Reverse Route Mileage',
'9827':'FLASHING BEACON',
'9828':'Military Road',
'9829':'Structure Name',
'9830':'Roadside Culture (Hiking Trail, etc.)',
'9831':'Route Address',
'9832':'END HIGH OCCUPANCY VEHICLE (HOV) LANE',
'9833':'BGN HIGH OCCUPANCY VEHICLE (HOV) LANE',
'9834':'END SCENIC ROAD',
'9835':'BGN SCENIC ROAD',
'9836':'End Route',
'9837':'End Overpass (Reverse Direction)',
'9838':'End Overpass (Log Direction)',
'9839':'Overpass Abandoned Railroad',
'9840':'Overpass Railroad',
'9841':'Underpass Abandoned Railroad',
'9842':'Underpass Railroad',
'9843':'Indian Reservation Road',
'9844':'END JUG HANDLE',
'9845':'BGN JUG HANDLE',
'9846':'Overpass (Building, Walkway, etc.)',
'9847':'Dr to Town Transfer Station',
'9848':'END COLL-DIST ROADWAY',
'9849':'BGN COLL-DIST ROADWAY',
'9850':'Auto Emissions Inspection Station',
'9851':'Traffic Count Location',
'9852':'END RUNAWAY TRUCK RAMP',
'9853':'BGN RUNAWAY TRUCK RAMP',
'9854':'Restricted Access',
'9855':'END DOT PERMIT (YEAR)',
'9856':'BGN DOT PERMIT (YEAR)',
'9857':'END PRIMARY ROUTE OVERLAP SECTION',
'9858':'BGN PRIMARY ROUTE OVERLAP SECTION',
'9859':'END PVMT OVERLAY(IM) OR END LIQ RES(HM)',
'9860':'BGN PVMT OVERLAY(IM) OR BGN LIQ RES(HM)',
'9861':'END MAINT.(VIP) OR CONSTR. PROJECT',
'9862 ':'BGN MAINT.(VIP) OR CONST. PROJECT',
'9863':'FIRE STATION FIRE HOUSE W/O SIGNAL',
'9864':'FIRE STATION FIRE HOUSE WITH SIGNAL',
'9865':'Commercial Drive (2-way) No Signal',
'9866':'Commercial Drive (Exit) No Signal',
'9867':'Commercial Drive (Entrance) No Signal',
'9868':'Signalized Commercial Drive (2-way)',
'9869':'Signalized Commercial Drive (Exit)',
'9870':'Signalized Commercial Drive (Entrance)',
'9871':'Traffic Recorder (Automatic)',
'9872':'Federal-State Agency(Post Office, Court, etc.)',
'9873':'Highway Boundary (CHD)',
'9874':'END BIKE LANE',
'9875':'BGN BIKE LANE',
'9876':'R.R. Depot',
'9877':'Bus Loading Area',
'9878':'Land Fill (Dump) Drive',
'9879':'Elevated Causeway',
'9880':'U.S.G.S. Monument',
'9881':'END TEMPORARY CONSTRUCTION OR ROUTING',
'9882':'BGN TEMPORARY CONSTRUCTION OR ROUTING',
'9884':'Truck Weighing Station',
'9885':'Maintenance Service Road',
'9886':'Tunnel',
'9887':'Service Area Exit (Food or Cars)',
'9888':'Service Area Entrance (Food or Cars)',
'9889':'Private Airport Road',
'9890':'Town/City Airport Road',
'9891':'State Airport Road',
'9892':'END RAMP SERVING AS MAIN LINE',
'9893':'BGN RAMP SERVING AS MAIN LINE',
'9894':'TOLL PLAZA CENTER LINE',
'9895':'Dam (Road over Dam)',
'9896':'Gate',
'9897':'Commuter Parking Lot Driveway',
'9898':'Median Crossover',
'9899':'End One-way Section',
'9900':'BGN ONE-WAY SECTION',
'9901':'End Separated Highway',
'9902':'Begin Separated Highway',
'9903':'End Divided Highway',
'9904':'Begin Divided Highway',
'9906':'Begin Interchange Area',
'9907':'Town Offices Driveway (Town Hall, Police, etc.)',
'9908':'Private Driveway',
'9909':'Multi-plate Pipe Arch Concrete Base',
'9910':'Underground Cable (Type) AT&T, etc.',
'9911':'END ACCELERATION LANE',
'9912':'BGN ACCELERATION LANE',
'9913':'Historical Monument',
'9914':'Parking Lot Drive (2-way)',
'9915':'Railroad Right-of-way (Tracks Removed)',
'9916':'Railroad Grade Crossing (Service Aband, Inactive)',
'9917':'Route Number or Street Name (R.I.)',
'9918':'Route Number or Street Name (N.Y.)',
'9919':'Route Number or Street Name (Mass.)',
'9920':'City Limits',
'9921':'Town Highway Garage Drive',
'9922':'Federal Institution Road',
'9923':'Military Reservation Road',
'9924':'Utility Pole',
'9925':'Two-Way Ramp(Unnumbered)',
'9926':'Stream (Structure Type Unknown)',
'9927':'END DECELERATION LANE',
'9928':'Begin Deceleration Lane',
'9929':'BGN TRAFFIC ISLAND',
'9930':'END TRAFFIC ISLAND',
'9931':'End Pavement Width Flare',
'9932':'Begin Pavement Width Flare',
'9933':'Mile Post or Measured Mile',
'9934':'State Line Sign',
'9935':'END ROTARY FLARE/ROUNDABOUT',
'9936':'BEGIN ROTARY FLARE/ROUNDABOUT',
'9937':'End State Maintenance',
'9938':'Approx. State Line (No Sign or Monument)',
'9939':'End Channelization',
'9940':'Begin Channelization',
'9941':'END STANCHIONS',
'9942':'Federal Aid Post',
'9943':'STATE FISH AND GAME ROAD(DEEP)',
'9944':'State Picnic or Rest Area Road or Drive',
'9945':'State Highway Storage Area Drive',
'9946':'State Highway Garage Drive',
'9947':'Borough Limits',
'9948':'Park Road (Town or City)',
'9949':'END TRUCK CLIMBING LANE(TCL/SVL)',
'9950':'BEGIN TRUCK CLIMBING LANE(TCL/SVL)',
'9951':'Parking Lot Drive (Entrance)',
'9952':'Parking Lot Drive (Exit)',
'9953':'END OVERLAP',
'9954':'BGN OVERLAP',
'9955':'Approx. Town Line (No Sign or Monument)',
'9956':'Town Line Sign',
'9957':'Road Under Construction',
'9958':'State Line Monument',
'9959':'Town Line Monument',
'9960':'BGN STANCHIONS',
'9961':'BGN TOWN MAINTENANCE',
'9962':'URBAN/RURAL LINE',
'9963':'RURAL/URBAN LINE',
'9964':'END TOWN MAINTENANCE',
'9965':'State Institution Road',
'9966':'School & Church Drive',
'9967':'Underpass (Building, Walkway, etc.)',
'9968':'"Primitive (""A"" Type) Road (Intersecting)"',
'9969':'Barricade',
'9970':'"""A"" Type (Primitive) Road (Back)"',
'9971':'"""A"" Type (Primitive) Road (Ahead)"',
'9972':'BOAT LAUNCHING DRIVE / FERRY',
'9973':'Telephone Cable',
'9974':'Proposed Road',
'9975':'BGN STATE MAINTENANCE',
'9976':'Actual State Line',
'9000 ':'OTHER TIEPOINT',
'9800 ':'Speed Bump',
'9801 ':'END LANE DROP',
'9802 ':'BGN LANE DROP',
'9804 ':'INCIDENT MANAGEMENT SERVICE CABINET',
'9805 ':'END TURN AROUND',
'9806 ':'BGN TURN AROUND',
'9807 ':'LOOPS',
'9808 ':'INFRA-RED BEAM/RADAR DET',
'9809 ':'TRAFFIC COUNTER CABINET',
'9810 ':'TRAFFIC SENSOR',
'9811 ':'LOOP COUNTERS',
'9812 ':'BGN ONE-WAY ALTERNATING TRAFFIC',
'9813 ':'END ONE-WAY ALTERNATING TRAFFIC',
'9814 ':'ITS CAMERA LOCATION',
'9815 ':'WEATHER STATION',
'9816 ':'BGN MOVABLE BRIDGE',
'9817 ':'END MOVABLE BRIDGE',
'9818 ':'OVERHEAD VMS SIGN',
'9819 ':'FLASHING SIGN',
'9820 ':'TRAFFIC SIGNAL',
'9821 ':'WIM LOCATIONS',
'9822 ':'CLASSIFICATION COUNTERS',
'9823 ':'MIDBLOCK PEDESTRIAN X-ING',
'9824 ':'MIDBLOCK PED X-ING W/DEVICES',
'9825 ':'Abandoned RR crossing (Tracks not removed)',
'9826 ':'End Reverse Route Mileage',
'9827 ':'FLASHING BEACON',
'9828 ':'Military Road',
'9829 ':'Structure Name',
'9830 ':'Roadside Culture (Hiking Trail, etc.)',
'9831 ':'Route Address',
'9832 ':'END HIGH OCCUPANCY VEHICLE (HOV) LANE',
'9833 ':'BGN HIGH OCCUPANCY VEHICLE (HOV) LANE',
'9834 ':'END SCENIC ROAD',
'9835 ':'BGN SCENIC ROAD',
'9836 ':'End Route',
'9837 ':'End Overpass (Reverse Direction)',
'9838 ':'End Overpass (Log Direction)',
'9839 ':'Overpass Abandoned Railroad',
'9840 ':'Overpass Railroad',
'9841 ':'Underpass Abandoned Railroad',
'9842 ':'Underpass Railroad',
'9843 ':'Indian Reservation Road',
'9844 ':'END JUG HANDLE',
'9845 ':'BGN JUG HANDLE',
'9846 ':'Overpass (Building, Walkway, etc.)',
'9847 ':'Dr to Town Transfer Station',
'9848 ':'END COLL-DIST ROADWAY',
'9849 ':'BGN COLL-DIST ROADWAY',
'9850 ':'Auto Emissions Inspection Station',
'9851 ':'Traffic Count Location',
'9852 ':'END RUNAWAY TRUCK RAMP',
'9853 ':'BGN RUNAWAY TRUCK RAMP',
'9854 ':'Restricted Access',
'9855 ':'END DOT PERMIT (YEAR)',
'9856 ':'BGN DOT PERMIT (YEAR)',
'9857 ':'END PRIMARY ROUTE OVERLAP SECTION',
'9858 ':'BGN PRIMARY ROUTE OVERLAP SECTION',
'9859 ':'END PVMT OVERLAY(IM) OR END LIQ RES(HM)',
'9860 ':'BGN PVMT OVERLAY(IM) OR BGN LIQ RES(HM)',
'9861 ':'END MAINT.(VIP) OR CONSTR. PROJECT',
'9862 ':'BGN MAINT.(VIP) OR CONST. PROJECT',
'9863 ':'FIRE STATION FIRE HOUSE W/O SIGNAL',
'9864 ':'FIRE STATION FIRE HOUSE WITH SIGNAL',
'9865 ':'Commercial Drive (2-way) No Signal',
'9866 ':'Commercial Drive (Exit) No Signal',
'9867 ':'Commercial Drive (Entrance) No Signal',
'9868 ':'Signalized Commercial Drive (2-way)',
'9869 ':'Signalized Commercial Drive (Exit)',
'9870 ':'Signalized Commercial Drive (Entrance)',
'9871 ':'Traffic Recorder (Automatic)',
'9872 ':'Federal-State Agency(Post Office, Court, etc.)',
'9873 ':'Highway Boundary (CHD)',
'9874 ':'END BIKE LANE',
'9875 ':'BGN BIKE LANE',
'9876 ':'R.R. Depot',
'9877 ':'Bus Loading Area',
'9878 ':'Land Fill (Dump) Drive',
'9879 ':'Elevated Causeway',
'9880 ':'U.S.G.S. Monument',
'9881 ':'END TEMPORARY CONSTRUCTION OR ROUTING',
'9882 ':'BGN TEMPORARY CONSTRUCTION OR ROUTING',
'9884 ':'Truck Weighing Station',
'9885 ':'Maintenance Service Road',
'9886 ':'Tunnel',
'9887 ':'Service Area Exit (Food or Cars)',
'9888 ':'Service Area Entrance (Food or Cars)',
'9889 ':'Private Airport Road',
'9890 ':'Town/City Airport Road',
'9891 ':'State Airport Road',
'9892 ':'END RAMP SERVING AS MAIN LINE',
'9893 ':'BGN RAMP SERVING AS MAIN LINE',
'9894 ':'TOLL PLAZA CENTER LINE',
'9895 ':'Dam (Road over Dam)',
'9896 ':'Gate',
'9897 ':'Commuter Parking Lot Driveway',
'9898 ':'Median Crossover',
'9899 ':'End One-way Section',
'9900 ':'BGN ONE-WAY SECTION',
'9901 ':'End Separated Highway',
'9902 ':'Begin Separated Highway',
'9903 ':'End Divided Highway',
'9904 ':'Begin Divided Highway',
'9906 ':'Begin Interchange Area',
'9907 ':'Town Offices Driveway (Town Hall, Police, etc.)',
'9908 ':'Private Driveway',
'9909 ':'Multi-plate Pipe Arch Concrete Base',
'9910 ':'Underground Cable (Type) AT&T, etc.',
'9911 ':'END ACCELERATION LANE',
'9912 ':'BGN ACCELERATION LANE',
'9913 ':'Historical Monument',
'9914 ':'Parking Lot Drive (2-way)',
'9915 ':'Railroad Right-of-way (Tracks Removed)',
'9916 ':'Railroad Grade Crossing (Service Aband, Inactive)',
'9917 ':'Route Number or Street Name (R.I.)',
'9918 ':'Route Number or Street Name (N.Y.)',
'9919 ':'Route Number or Street Name (Mass.)',
'9920 ':'City Limits',
'9921 ':'Town Highway Garage Drive',
'9922 ':'Federal Institution Road',
'9923 ':'Military Reservation Road',
'9924 ':'Utility Pole',
'9925 ':'Two-Way Ramp(Unnumbered)',
'9926 ':'Stream (Structure Type Unknown)',
'9927 ':'END DECELERATION LANE',
'9928 ':'Begin Deceleration Lane',
'9929 ':'BGN TRAFFIC ISLAND',
'9930 ':'END TRAFFIC ISLAND',
'9931 ':'End Pavement Width Flare',
'9932 ':'Begin Pavement Width Flare',
'9933 ':'Mile Post or Measured Mile',
'9934 ':'State Line Sign',
'9935 ':'END ROTARY FLARE/ROUNDABOUT',
'9936 ':'BEGIN ROTARY FLARE/ROUNDABOUT',
'9937 ':'End State Maintenance',
'9938 ':'Approx. State Line (No Sign or Monument)',
'9939 ':'End Channelization',
'9940 ':'Begin Channelization',
'9941 ':'END STANCHIONS',
'9942 ':'Federal Aid Post',
'9943 ':'STATE FISH AND GAME ROAD(DEEP)',
'9944 ':'State Picnic or Rest Area Road or Drive',
'9945 ':'State Highway Storage Area Drive',
'9946 ':'State Highway Garage Drive',
'9947 ':'Borough Limits',
'9948 ':'Park Road (Town or City)',
'9949 ':'END TRUCK CLIMBING LANE(TCL/SVL)',
'9950 ':'BEGIN TRUCK CLIMBING LANE(TCL/SVL)',
'9951 ':'Parking Lot Drive (Entrance)',
'9952 ':'Parking Lot Drive (Exit)',
'9953 ':'END OVERLAP',
'9954 ':'BGN OVERLAP',
'9955 ':'Approx. Town Line (No Sign or Monument)',
'9956 ':'Town Line Sign',
'9957 ':'Road Under Construction',
'9958 ':'State Line Monument',
'9959 ':'Town Line Monument',
'9960 ':'BGN STANCHIONS',
'9961 ':'BGN TOWN MAINTENANCE',
'9962 ':'URBAN/RURAL LINE',
'9963 ':'RURAL/URBAN LINE',
'9964 ':'END TOWN MAINTENANCE',
'9965 ':'State Institution Road',
'9966 ':'School & Church Drive',
'9967 ':'Underpass (Building, Walkway, etc.)',
'9968 ':'"Primitive (""A"" Type) Road (Intersecting)"',
'9969 ':'Barricade',
'9970 ':'"""A"" Type (Primitive) Road (Back)"',
'9971 ':'"""A"" Type (Primitive) Road (Ahead)"',
'9972 ':'BOAT LAUNCHING DRIVE / FERRY',
'9973 ':'Telephone Cable',
'9974 ':'Proposed Road',
'9975 ':'BGN STATE MAINTENANCE',
'9976 ':'Actual State Line'
}

tiepoint_type_lookup = {
  
    '1':'Railroad Crossing',
'2':'Railroad Crossing',
'3':'Railroad Crossing',
'4':'Railroad Crossing',
'5':'Railroad Crossing',
'6':'Railroad Crossing',
'7':'Railroad Crossing',
'8':'Railroad Crossing',
'9':'Railroad Crossing',
'A':'STRUCTURE',
'B':'SNET Poles (Southern New England Telephone Company)',
'C':'HELCO Poles (Hartford Electrical Light Company)',
'D':'CL&P Poles (Conn. Lignt and Power Company)',
'E':'CP Poles (Conn. Power Company)',
'F':'UI Poles (United Illuminating Company)',
'G':'BL&P Poles (Bozrah Light & Power Company)',
'H':'FRP Poles (Farmington River Power Company)',
'I':'GDU Poles (City of Groton, Dept. of Utilities)',
'J':'JCEL Poles (Jewett City Electrical Light Plant)',
'K':'NPUD Poles (Norwich Dept. of Public Utilities)',
'L':'NED Poles (Norwalk Electric Department)',
'M':'SNEW Poles (South Norwalk Electric Works)',
'N':'WED Poles (Wallingford Electric Dept.)',
'O':'WTCO Poles (Woodbury Telephone Company)',
'P':'NYTCO Poles (New York Telephone Company)',
'Q':'AT&T Poles (American Telephone & Telegraph Company)',
'R':'VCV (Valley Cable Vision)',
'S':'BEW (Borough Electric Work)',
'T':'GW&E (Groton Water & Electric)',
'X':'Posted Exit Numbers'
}

bridge_prefix_lookup = {
    
    'L':'Local (not on above systems)',
'P':'FAP',
'S':'FAS',
'T':'FAP-U Type II (TOPICS)',
'U':'Urban Systems',
'Z':'Pipes, pipe and plate arches, etc.'
}

bridge_location_lookup = {
  
"L":"Log",
"R":"Reverse"
}

hw_log_code_lookup = {
 
    '01':'Multiple',
'02':'Structures',
'03':'Railroad Crossing',
'99':'TEST DO NOT USE'
}

fed_aid_lookup = {
   
    '1':'IS (Chargeable to FAP System)',
'2':'FAP',
'3':'FAP, serving as IS tr-way',
'4':'FAS, serving as IS tr-way',
'5':'FAS (rural Only)',
'6':'NFA',
'7':'NFA, serving as IS tr-way',
'8':'IS (Non-chargeable to FAP System) (Addition to IS) (23, USC 139)',
'9':'NFA, not IS, serving as FAP tr-way',
'A':'Frontage Road, IS',
'B':'Frontage Road, FAP',
'C':'Frontage Road, FAS',
'D':'Frontage Road, NFA',
'F':'FAU System',
'G':'FAU System serving as IS tr-way',
'H':'FAU System serving as FAP tr-way',
'I':'FAS, serving as FAP tr-way',
'J':'IS Secretarial Agreement'
}
functional_class_lookup = {
 
    '1':'INTERSTATE',
'2':'Other Principal Arterial',
'3':'Minor Arterial',
'4':'Major Collector (Rural)',
'5':'Minor Collector (Rural Only)',
'6':'Local Usage',
'7':'LOCAL USAGE-NEW HPMS',
' 1':'INTERSTATE',
' 2':'Other Principal Arterial',
' 3':'Minor Arterial',
' 4':'Major Collector (Rural)',
' 5':'Minor Collector (Rural Only)',
' 6':'Local Usage',
' 7':'LOCAL USAGE-NEW HPMS',
'11':'Interstate',
'12':'Other Freeway or Expressway',
'13':'Other Principal Arterial',
'14':'Minor Arterial',
'15':'Major Collector (Urban)',
'16':'Local Usage',
'21':'Interstate',
'22':'Other Freeway or Expressway',
'23':'Other Principal Arterial',
'24':'Minor Arterial',
'25':'Major Collector (Urban)',
'26':'Local Usage',
'31':'Interstate',
'32':'Other Freeway or Expressway',
'33':'Other Principal Arterial',
'34':'Minor Arterial',
'35':'Major Collector (Urban)',
'36':'Local Usage',
'41':'Interstate',
'42':'Other Freeway or Expressway',
'43':'Other Principal Arterial',
'44':'Minor Arterial',
'45':'Major Collector (Urban)',
'46':'Local Usage'
}
admin_system_lookup= {
    
    '0':'State Maintained, not on state system (legislative)',
'1':'State Primary (State Maintained)',
'2':'State Secondary (State Maintained)',
'4':'State Special Service (State Maintained)',
'5':'Ramps, Turning Roadways or Connectors',
'7':'Ramp or TR Serving as mainline, state primary',
'8':'Ramp serving as mainline, state secondary',
'9':'Ramp serving as mainline, state special service',
'A':'State Maintained Stubs & Bypassed section (State Secondary)',
'B':'Proposed location, State',
'C':'New Construction, built not open to traffic, State',
'H':'Frontage Road',
'I':'State Park and Forest',
'J':'State institution road',
'O':'Temporary Routing',
'P':'Proposed, Local',
'Q':'Built not open, Local',
'R':'Ramp or TR, built not open',
'X':'Closed to Traffic'
}
urban_area_lookup = {
 
    'A':'BRIDGEPORT - STAMFORD',
'B':'NEW YORK - NEWARK',
'C':'DANBURY',
'D':'HARTFORD',
'G':'NEW HAVEN',
'H':'NORWICH - NEW LONDON',
'K':'WATERBURY',
'L':'COLCHESTER',
'M':'DANIELSON',
'N':'LAKE POCOTOPAUG',
'O':'STORRS',
'P':'TORRINGTON',
'Q':'WILLIMANTIC',
'R':'WINSTED',
'S':'WORCESTER',
'T':'SPRINGFIELD',
'U':'STAFFORD',
'V':'JEWETT CITY',
'Y':'Rural Census Place 2,500 Population or Greater',
'Z':'Rural Census Place Under 2,500 Population'
}
highway_type_lookup = {
  
    '1':"2 LANE CONTIGUOUS (WIDTH UNDER 36')",
'2':"2 LANES DIVIDED (WIDTH UNDER 36')",
'3':"3 OR MORE LANES CONTIGUOUS (WIDTH 30' OR MORE)",
'4':"3-4 LANES DIVIDED (WIDTH 36'-71')",
'5':"6-7 LANES DIVIDED (WIDTH 72'-95')",
'6':"8 LANES DIVIDED (WIDTH 96'-119')",
'7':"10 LANES DIVIDED (WIDTH 120'-143')",
'8':"12 OR MORE LANES DIVIDED (WIDTH 144' OR MORE)",
'9':"one-way traffic",
'A':"ALTERNATING ONE-WAY"
}
highway_acc_lookup = {
 
    '1':'NONE',
'2':'Partial',
'3':'Full, not expressway or freeway',
'4':'Full, expressway or freeway',
'5':'Full, parkway (trucks not permited)',
'6':'Channelization, access controlled, incl. Rotary intersection, underpass or overpass controlled highway',
'7':"Full, ramps, TR's HOV lanes, (not main line)",
'8':'Full Pkwy. Trucks permitted (full control)'
}
on_sys_method_lookup = {
  
    '0':'No Data',
'1':'New Highway over new line',
'2':'State Highway accepted from town',
'3':'State Highway accepted from town and reconstructed',
'4':'Accepted from other State Agency'
}
lim_access_lookup = {
  
    '0':'End Limit of mileage on limited access report',
'1':'Full Control Parkways',
'2':'Full Control - Other Divided Highways, 4 or more lanes',
'3':'Full Control - Divided, 2 lanes',
'4':'Full Control - Undivided Higways',
'5':'Partial Control - Divided, 4 or more lanes',
'6':'Partial Control - Undivided Highways',
'7':'Partial Control - Channelization'
}
special_system_code_lookup = {
  
    '0':'',
'1':'Federal Aid Priority Primary',
'2':'Defense Access Highway',
'3':'Economic Growth Center Development Highway',
'4':'Scenic Highway',
'5':'STRATEGIC HIGHWAY NETWORK (STRAHNET)',
'6':'PRIMARY ROUTE OVER LAP SECTION'
}
rl_alt_lookup = {
  
    "0":"Regular Route",
    "1":"Alternate Route A"
}
fc_link_lookup = {
  
    "1":"Connecting link (Rural principal arterial)",
    "2":"Connecting link (Rural minor arterial)"
}
pavement_type_lookup = {

    '0002':'B - PRIMITIVE',
'0010':'C - GRADED & DRAINED EARTH',
'1000':'D - SOILED SURFACED',
'2010':'E- GRAVEL OR STONE WITHOUT STABILIZING ADMIXTURE, ON GRADED & DRAINED EARTH',
'3010':'Bit. Surf.-On graded & drained earth',
'3210':'Bit. Surf.-On gravel or stone',
'4131':'Mixed Bit. On soil (7'' &>thickness)',
'4221':'Mixed Bit. On gravel or stone (<7'' thickness)',
'4231':'Mixed Bit. On gravel or stone (7'' &>thickness)',
'4921':'Mix on bit.tr.pen.or bit.conc. on gravel or stone',
'4922':'Mix on mixed bit. on gravel or stone',
'4976':'Mix on old concrete',
'5001':'BIT & PEN ON GRADED & DRAINED EARTH',
'5241':'Bit. & pen. on soil',
'5251':'Bit. and Pen. On gravel or stone',
'6001':'Bit. Conc. - base unknown',
'6101':'Bit. Conc. On soil',
'6201':'Bit. Conc. On bit. Pen. On gravel or stone',
'6705':'Bit. Pre-stressed Bit. bridge deck, hollowed inside',
'6706':'Bit Conc. On old concrete',
'6707':'Bit Conc. On new concrete',
'6708':'Bit Conc. On reinforced concrete (bridge)',
'6805':'Bit Conc. On old brick on non-rigid sub-base',
'6806':'Bit Conc. On old block on non-rigid sub-base',
'6807':'Bit Conc. On old brick on concrete sub-base',
'7001':'Plain Conc. On graded & drained earth',
'7021':'Reinforced Conc. On graded & drained earth',
'7201':'Plain Conc. On gravel or stone',
'7221':'Reinforced Conc. On gravel or stone',
'7726':'Concrete, reinforced, on old concrete',
'7900':'CONCRETE, REINFORCED, BRIDGE DECK',
'7905':'Prre-stressed Conc. Bridge deck, hollowed inside',
'7906':'Steel grate filled with concrete',
'7907':'Open steel grate',
'8301':'BRICK ON NON-RIGID BASE',
'9100':'Wood Deck'
}
surface_thickness_lookup = {
    'A':'"0.5"" and less than 1"""',
'B':'"1"" and less than 1.5"""',
'C':'"1.5"" and less than 2"""',
'D':'"2"" and less than 2.5"""',
'E':'"2.5"" and less than 3"""',
'F':'"3"" and less than 3.5"""',
'G':'"3.5"" and less than 4"""',
'H':'"4"" and less than 4.5"""',
'I':'"4.5"" and less than 5"""',
'J':'"5"" and less than 5.5"""',
'K':'"5.5"" and less than 6"""',
'L':'"6"" and less than 6.5"""',
'M':'"6.5"" and less than 7"""',
'N':'"7"" and less than 7.5"""',
'O':'"7.5"" and less than 8"""',
'P':'"8"" and less than 8.5"""',
'Q':'"8.5"" and less than 9"""',
'R':'"9"" and less than 10"""',
'S':'"10"" and Over"'
}
base_thickness_lookup={
    'A':'"less than 2"""',
'B':'"2"" and less than 3"""',
'C':'"3"" and less than 4"""',
'D':'"4"" and less than 5"""',
'E':'"5"" and less than 6"""',
'F':'"6"" and less than 7"""',
'G':'"7"" and less than 8"""',
'H':'"8"" and less than 9"""',
'I':'"9"" and less than 10"""',
'J':'"10"" and less than 11"""',
'K':'"11"" and less than 12"""',
'L':'"12"" and less than 13"""',
'M':'"13"" and less than 14"""',
'N':'"14"" and less than 15"""',
'O':'"15"" and over"'
}
improve_type_lookup = {
    '0':'No data',
'1':'Reconstruction, replacing pavement',
'2':'"Resurfacing 1"" or more in thickness"',
'3':'Accepted, no construction involved',
'4':'Maint. (any construction by State Forces)',
'5':'Acceptance (prior to conversion date, before 1975)',
'6':'Accepted and reconstructed immediatly',
'7':'Construction on new location (new highway)',
'8':'"2.5"" or less milled off"',
'9':'"more than 2.5"" milled off"',
'A':'RECLAIM EXISTING PVMT',
'B':'"RESURFACING 1/2"" TO LESS THAN 1"" IN THICKNESS"'
}
improve_location_lookup = {
    'A':'Thru lanes',
'B':'Thru lanes (Bridge Deck)',
'C':'Toll Plazas',
'D':'Widening, right side of contiguous or outside divided',
'E':'Widening, left side of contiguous or inside of divided',
'F':'Widening, location unknown',
'G':'High occupancy vehicle (HOV) lane',
'H':'WIDENING, BOTH SIDES OF CONTIGUOUS OR DIVIDED ROAD'
}
hpms_median_type_lookup = {
    '0':'No Data',
'1':'Raised',
'2':'Raised with Barrier',
'3':'Depressed',
'4':'Depressed with Barrier',
'5':'Separated Roadway',
'6':'SEPARATED ROADWAY WITH BARRIER',
'7':'Rotary',
'8':'Traffic Island',
'9':'PAINTED CHANNELIZATION',
'A':'MP CONC BARRIER',
'B':'Bi-level Structure (Upper Level)',
'C':'Bi-level Structure (Lower Level)',
'D':'FLUSH, OR OTHER',
'E':'OPEN MEDIAN W/ BARRIER (STRUCTURES)',
'F':'Jersey Type (Conc. Wall)'
}
maint_type_lookup = {
    '2':'MICRO/DIAMOND MILLING',
'3':'MICRO-SURFACING(MS)',
'4':'NOVA CHIP (NC)',
'5':'Armor -Liquid Res (HM)',
'6':'Bit.Conc.(IM)'
}
curb_lookup = {
    '-':'Curbing Ends',
'0':'No Data',
'1':'Bituminous Concrete Lip Mountable (M) Curb (MI)',
'2':'Concrete Lip Mountable (M) Curb (MJ)',
'3':'Granite Slope (M) Curb (MG)',
'4':'Concrete Vertical (V) Curb (VJ)',
'5':'Granite Vertical (V) Curb (VG)'
}
shoulder_pavement_lookup={
    '00':'No Data',
'B ':'Primitive',
'C ':'Graded & Drained Earth',
'D ':'Soil Surfaced',
'E ':'Gravel or Stone',
'F ':'Bituminous Surface Treated',
'FM':'Oil and Sand',
'G ':'Mixed Bituminous',
'H ':'Bituminous Penetration',
'HM':'Armor - Liquid Res. (HM)',
'I ':'Bituminous Concrete',
'IM':'"Bituminous Concrete (less than 1"" thick)"',
'J ':'Concrete',
'K ':'Brick',
'L ':'Block',
'MS':'MICRO-SURFACING',
'NC':'NOVA CHIP',
'O ':'No Shoulder or Auxiliary Lane',
'SG':'OPEN STEEL GRID',
'SJ':'STEEL GRATE FILLED IN WITH CONCRETE',
'XX':'PRIMITIVE'
}
aux_lane_type_lookup = {
    '0':'No Data',
'1':'Slow lane',
'2':'Acceleration Lane',
'3':'Deceleration Lane',
'4':'Weaving Lane',
'5':'Turning Lane',
'7':'High Occupancy Vehicle Lane (HOV Lane)',
'8':'Single Lane 2-Way Left Turn Lane',
'9':'Continuous Left Turn Lane in Alternating Directions',
'M':'Multiple Auxiliary Lane Type'
}
one_way_lookup = {
    "1":"One-way North or One-Way East",
    "2":"One-way South or One-Way West",
    "-":"End of One-Way section",
    "A":"One-way alternating direction"
}
system_maintenance_lookup = {
    "0":"Local Road",
    "D":"Locally Maintained, State Primary",
    "E":"Locally Maintained, State Secondary",
    "F":"Locally Maintained, Special Service",
    "G":"Not on State Maintained System"
}

rural_urban_lookup = {
"5":"Rural Town",
"6":"Urban Town",
"7":"Urban Borough",
"8":"Rural Borough"
}

r_u_designation_lookup = {
    "1":"Rural",
    "2":"Urban"
}

# single class insert lookup. make dynamic so you can just change the inputs to put in the position you want

#Intersecting Road??? maybe grab from the drop down

def year_formatter(year):
    try:
        ayear = int(year.lstrip().rstrip())
        if ayear >= 0 and ayear <= 22:
            ayear = ayear+2000
        elif ayear >=23 and ayear <= 99:
            ayear = ayear + 1900
        return str(ayear)
    except ValueError:
        return year

class Lookup(BoxLayout):
    def __init__(self,r_u_designation=False,rural_urban = False,system_maintenance=False,one_way=False,aux_lane_type=False,shoulder_pavement=False,curb=False,maint_type = False,hpms_median_type=False,improve_location=False,improve_type = False,base_thickness=False,surface_thickness=False,pavement_type=False,fc_link=False,rl_alt=False,special_system_code=False,lim_access=False,on_sys_method=False,highway_acc=False,highway_type=False,urban_area=False,admin_system=False,functional_class=False,fed_aid = False,the_input=None,town=False,road_type=False,road_class=False,road_status=False,tiepoint_code=False,tiepoint_type=False,bridge_prefix=False,bridge_location=False,hw_log_code=False,**kwargs):
        super(Lookup, self).__init__(**kwargs)
        #BoxLayout.__init__(self)
        self.the_input = the_input
        self.r_u_designation=True
        self.rural_urban = rural_urban
        self.system_maintenance=system_maintenance
        self.one_way=one_way
        self.aux_lane_type=aux_lane_type
        self.shoulder_pavement=shoulder_pavement
        self.curb=curb
        self.maint_type = maint_type
        self.hpms_median_type = hpms_median_type
        self.improve_location = improve_location
        self.improve_type = improve_type
        self.base_thickness=base_thickness
        self.surface_thickness=surface_thickness
        self.pavement_type=pavement_type
        self.on_sys_method=on_sys_method
        self.urban_area=urban_area
        self.highway_type=highway_type
        self.functional_class=functional_class
        self.fed_aid = fed_aid
        self.town=town
        self.road_type = road_type
        self.road_class = road_class
        self.road_status = road_status
        self.tiepoint_code = tiepoint_code
        self.tiepoint_type = tiepoint_type
        self.bridge_prefix = bridge_prefix
        self.bridge_location =bridge_location
        self.hw_log_code = hw_log_code
        self.admin_system=admin_system
        self.highway_acc=highway_acc
        self.lim_access=lim_access
        self.special_system_code=special_system_code
        self.rl_alt=rl_alt
        self.fc_link = fc_link

        if len(self.the_input.rstrip().lstrip())==0:
    
            button = Button(text="-",background_color=(1,0,0,1),disabled = True)
            button.bind(on_press=self.lookup)
            self.add_widget(button)
        else:
            button = Button(text="-",background_color=(0,1,0,1))
            button.bind(on_press=self.lookup)
            self.add_widget(button)
        
        
        
    def lookup(self,*args):
        
        adict = {}
        if self.town:
            adict = town_lookup
        elif self.road_type:
            adict = road_type_lookup
        elif self.road_class:
            adict = road_class_lookup
        elif self.road_status:
            adict = road_status_lookup
        elif self.tiepoint_code:
            adict=tiepoint_code_lookup
        elif self.tiepoint_type:
            adict = tiepoint_type_lookup
        elif self.bridge_prefix:
            adict=bridge_prefix_lookup
        elif self.bridge_location:
            adict=bridge_location_lookup
        elif self.hw_log_code:
            adict=hw_log_code_lookup
        elif self.fed_aid:
            adict=fed_aid_lookup
        elif self.functional_class:
            adict=functional_class_lookup
        elif self.admin_system:
            adict=admin_system_lookup
        elif self.urban_area:
            adict=urban_area_lookup
        elif self.highway_type:
            adict=highway_type_lookup
        elif self.highway_acc:
            adict=highway_acc_lookup
        elif self.on_sys_method:
            adict=on_sys_method_lookup
        elif self.lim_access:
            adict=lim_access_lookup
        elif self.special_system_code:
            adict=special_system_code_lookup
        elif self.rl_alt:
            adict=rl_alt_lookup
        elif self.fc_link:
            adict=fc_link_lookup
        elif self.pavement_type:
            adict=pavement_type_lookup
        elif self.surface_thickness:
            adict=surface_thickness_lookup
        elif self.base_thickness:
            adict=base_thickness_lookup
        elif self.improve_type:
            adict=improve_type_lookup
        elif self.improve_location:
            adict=improve_location_lookup
        elif self.hpms_median_type:
            adict=hpms_median_type_lookup
        elif self.maint_type:
            adict=maint_type_lookup
        elif self.curb:
            adict=curb_lookup
        elif self.shoulder_pavement:
            adict=shoulder_pavement_lookup
        elif self.aux_lane_type:
            adict=aux_lane_type_lookup
        elif self.one_way:
            adict=one_way_lookup
        elif self.system_maintenance:
            adict=system_maintenance_lookup
        elif self.rural_urban:
            adict=rural_urban_lookup
        elif self.r_u_designation:
            adict=r_u_designation_lookup


        input_text=""
        try:
            input_text=adict[self.the_input]
        except KeyError:
            pass
        popup = Popup(title = "Lookup",content = Label(text=input_text),auto_dismiss=True,size=(400,400),size_hint=(None,None))
        popup.open()
    
        

    

def create_town_df(ascii_file_path):
    adict = {"Line":[],
            "Card Number":[],
            "Milepoint":[],
            "Road Number":[],
            "Road Name":[],
            "Town Number":[],
            "Road_Num+Desc":[]
            }
    f = open(ascii_file_path,"r")
    for i in f:
        adict["Line"].append(i)
        adict["Milepoint"].append(i[22:28])
        adict["Card Number"].append(i[28:30])
        adict["Road Number"].append(i[3:7].rstrip())
        adict["Road Name"].append(i[30:54].rstrip())
        adict["Town Number"].append(i[0:3])
        adict["Road_Num+Desc"].append(i[3:7].rstrip()+"-"+i[30:54].rstrip())
    f.close()

    df = pd.DataFrame(adict)
    return df

def get_unique_towns(df):
    return df["Town Number"].unique().tolist()

def get_unique_routes_per_town(town,df):
    return df[(df["Town Number"]==town) & (df["Card Number"]=="41")]["Road_Num+Desc"].unique().tolist()

def get_unique_mp_per_route_per_town(town,route,df):
    return df[(df["Town Number"]==town) & (df["Road Number"]==route[0:4])]["Milepoint"].unique().tolist()

def get_top_data_town(town,route,df):
    get_milepoints = df[(df["Town Number"]==town) & (df["Road Number"]==route[0:4])].reset_index()

    Road_Name = get_milepoints.at[0,"Line"][30:54].rstrip()
    Direction = get_milepoints.at[0,"Line"][10]
    Grid_Letter = get_milepoints.at[0,"Line"][65:67].rstrip().lstrip()
    Grid_Number = get_milepoints.at[0,"Line"][67:69].rstrip().lstrip()
    return {"Road Name":Road_Name,
            "Direction":Direction,
            "Grid_Letter":Grid_Letter,
            "Grid_Number":Grid_Number}

def get_rest_of_data_town(choose_town,choose_route,choose_milepoint,df):

    sub_df = df[(df["Town Number"]==choose_town) & (df["Road Number"]==choose_route[0:4])].reset_index()

    Latitude = ""
    Longitude = ""
    Node_Number = ""
    Node_Code = ""
    #Administration
    Nhs = ""
    HPMS_Prefix = ""
    HPMS_Number = ""
    HPMS_Subdivision = ""
    HPMS_Month = ""
    HPMS_Year = ""
    ADT_Sample = ""
    ADT_Volume = ""
    ADT_Year = ""
    Urban_Area = ""
    Fc = ""
    One_Way = ""
    # Pavement Configuration
    Left_Curb = ""
    Left_Outside_Shoulder_Width = ""
    Left_Outside_Shoulder_Pavement = ""
    Left_Travel_Way_Width = ""
    Left_Travel_Way_Pavement = ""
    Left_Inside_Shoulder_Width = ""
    Left_Inside_Shoulder_Pavement = ""
    Total_Paved_Width=""
    Median_Width = ""
    Right_Travel_Way_Width=""
    Right_Travel_Way_Pavement=""
    Right_Outside_Shoulder_Width = ""
    Right_Outside_Shoulder_Pavement = ""
    Right_Inside_Shoulder_Width = ""
    Right_Inside_Shoulder_Pavement = ""
    Right_Curb=""
    Number_of_Through_Lanes = ""
    On_Sys_Year = ""
    Rural_Urban_Code = ""
    System_Maint= ""
    Inv_Year = ""
    #TIEPOINTS
    Tiepoints_Town = {}
    for i in range(sub_df.shape[0]):
        if sub_df.at[i,"Card Number"]=="50" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb = sub_df.at[i,"Line"][35]
            Left_Outside_Shoulder_Width = sub_df.at[i,"Line"][36:38]
            Left_Outside_Shoulder_Pavement = sub_df.at[i,"Line"][38:40]
            Left_Travel_Way_Width = sub_df.at[i,"Line"][44:46]
            Left_Travel_Way_Pavement = sub_df.at[i,"Line"][46:48]
            Left_Inside_Shoulder_Width = sub_df.at[i,"Line"][48:50]
            Left_Inside_Shoulder_Pavement = sub_df.at[i,"Line"][50:52]
            Total_Paved_Width = sub_df.at[i,"Line"][32:35]
            Median_Width = sub_df.at[i,"Line"][52:55]
            Right_Travel_Way_Width = sub_df.at[i,"Line"][60:62]
            Right_Travel_Way_Pavement = sub_df.at[i,"Line"][62:64]
            Right_Outside_Shoulder_Width = sub_df.at[i,"Line"][68:70]
            Right_Outside_Shoulder_Pavement = sub_df.at[i,"Line"][70:72]
            Right_Inside_Shoulder_Width = sub_df.at[i,"Line"][56:58]
            Right_Inside_Shoulder_Pavement = sub_df.at[i,"Line"][58:60]
            Right_Curb=sub_df.at[i,"Line"][72]
            Number_of_Through_Lanes=sub_df.at[i,"Line"][65:67]
            On_Sys_Year = sub_df.at[i,"Line"][73:75]
            Rural_Urban_Code = sub_df.at[i,"Line"][75]
            System_Maint = sub_df.at[i,"Line"][77]
            Inv_Year = sub_df.at[i,"Line"][30:32]
        if sub_df.at[i,"Card Number"]=="42" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Latitude = sub_df.at[i,"Line"][80:89]
            Longitude = sub_df.at[i,"Line"][89:98]
        if sub_df.at[i,"Card Number"]=="53" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Node_Number = sub_df.at[i,"Line"][32:40]
            Node_Code = sub_df.at[i,"Line"][41]
        if sub_df.at[i,"Card Number"]=="51" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Nhs = sub_df.at[i,"Line"][30]
            HPMS_Prefix = sub_df.at[i,"Line"][33]
            HPMS_Number = sub_df.at[i,"Line"][34:37]
            HPMS_Subdivision = sub_df.at[i,"Line"][37]
            HPMS_Month = sub_df.at[i,"Line"][39:41]
            HPMS_Year = sub_df.at[i,"Line"][41:43]
            ADT_Sample = sub_df.at[i,"Line"][56]
            ADT_Volume = sub_df.at[i,"Line"][57:63]
            ADT_Year = sub_df.at[i,"Line"][63:65]
            Urban_Area = sub_df.at[i,"Line"][65]
            Fc = sub_df.at[i,"Line"][75:77]
            One_Way = sub_df.at[i,"Line"][78]
        if int(sub_df.at[i,"Card Number"]) >= 42 and int(sub_df.at[i,"Card Number"]) <=49 and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Intersection_Desc = sub_df.at[i,"Line"][30:54].rstrip()
            Intersecting_Route = ""
            Intersecting_Road = ""
            Intersecting_Town = ""
            Tiepoint_Code = ""
            Connector = sub_df.at[i,"Line"][61]
            Connector_Count = sub_df.at[i,"Line"][62:64]
            Angle = sub_df.at[i,"Line"][76:78]
            Bridge_Number = sub_df.at[i,"Line"][65:71]
            Bridge_Suffix = sub_df.at[i,"Line"][71]
            if sub_df.at[i,"Line"][57]=="9":
                Tiepoint_Code = sub_df.at[i,"Line"][57:61]
            if len(sub_df.at[i,"Line"][54:57].rstrip().lstrip()) == 0:
                # its state therefore
                Intersecting_Route = sub_df.at[i,"Line"][58:61]
            if len(sub_df.at[i,"Line"][54:57].rstrip().lstrip()) != 0 and sub_df.at[i,"Line"][57]!="9":
                Intersecting_Town = sub_df.at[i,"Line"][54:57]
                Intersecting_Road = sub_df.at[i,"Line"][57:61]
            if len(sub_df.at[i,"Line"][54:57].rstrip().lstrip()) != 0 and sub_df.at[i,"Line"][57]=="9":
                Intersecting_Town = sub_df.at[i,"Line"][54:57]

            if Intersection_Desc in Tiepoints_Town:
                for i in range(1,100):
                    if Intersection_Desc +"_"+str(i) not in Tiepoints_Town:
                        Intersection_Desc = Intersection_Desc + "_"+str(i)
                        break
            leg_bridge_name = ""
        #
            if "BGN OP I-84 & UNION ST" in Intersection_Desc and sub_df.at[i,"Milepoint"]=="000160":
                leg_bridge_name = "ROBERTO CLEMENTE MEM BRIDGE"
                Tiepoints_Town["ROBERTO CLEMENTE MEM BRIDGE"] = {"Intersecting Desc":"ROBERTO CLEMENTE MEM BRIDGE",
                                            "Intersecting Route":"",
                                            "Intersecting Town":"151",
                                            "Intersecting Road":"",
                                            "Connector":"",
                                            "Connector Count":"",
                                            "Tiepoint Code":"9988",
                                            "Angle":"00",
                                            "Bridge Number":"04318",
                                            "Bridge Suffix": "",
                                            "Leg. Bridge Name":leg_bridge_name

                                            }
            if "OP I-84-YANKEE EXPWY" in Intersection_Desc and sub_df.at[i,"Milepoint"]=="000450":
                leg_bridge_name = "AVENUE OF HEROES BRIDGE"
                Tiepoints_Town["AVENUE OF HEROES BRIDGE"] = {"Intersecting Desc":"AVENUE OF HEROES BRIDGE",
                                            "Intersecting Route":"",
                                            "Intersecting Town":"151",
                                            "Intersecting Road":"",
                                            "Connector":"",
                                            "Connector Count":"",
                                            "Tiepoint Code":"9988",
                                            "Angle":"00",
                                            "Bridge Number":"03207",
                                            "Bridge Suffix": "",
                                            "Leg. Bridge Name":leg_bridge_name

                                            }
            if "OP I-95" in Intersection_Desc and sub_df.at[i,"Milepoint"]=="001040":
                leg_bridge_name = "KHALIQ SANDA MEM BRIDGE"
                Tiepoints_Town["KHALIQ SANDA MEM BRIDGE"] = {"Intersecting Desc":"KHALIQ SANDA MEM BRIDGE",
                                            "Intersecting Route":"",
                                            "Intersecting Town":"158",
                                            "Intersecting Road":"",
                                            "Connector":"",
                                            "Connector Count":"",
                                            "Tiepoint Code":"9929",
                                            "Angle":"00",
                                            "Bridge Number":"",
                                            "Bridge Suffix": "",
                                            "Leg. Bridge Name":leg_bridge_name

                                            }
            Tiepoints_Town[Intersection_Desc]={"Intersecting Desc":Intersection_Desc,
                                            "Intersecting Route":Intersecting_Route,
                                            "Intersecting Town":Intersecting_Town,
                                            "Intersecting Road":Intersecting_Road,
                                            "Connector":Connector,
                                            "Connector Count":Connector_Count,
                                            "Tiepoint Code":Tiepoint_Code,
                                            "Angle":Angle,
                                            "Bridge Number":Bridge_Number,
                                            "Bridge Suffix": Bridge_Suffix,
                                            "Leg. Bridge Name":leg_bridge_name

                                            }
    return {
        "Top":{"Latitude":Latitude,
                "Longitude":Longitude,
                "Node Number":Node_Number,
                "Node Code":Node_Code},
        "Administration":{"NHS":Nhs,
                            "HPMS Prefix":HPMS_Prefix,
                            "HPMS Number":HPMS_Number,
                            "HPMS Subdivision":HPMS_Subdivision,
                            "HPMS Month":HPMS_Month,
                            "HPMS Year":year_formatter(HPMS_Year),
                            "ADT Sample":ADT_Sample,
                            "ADT Volume":ADT_Volume,
                            "ADT Year":year_formatter(ADT_Year),
                            "Urban Area":Urban_Area,
                            "Funct. Class":Fc,
                            "One Way":One_Way},
        "Pavement Configuration":{"Left Curb":Left_Curb,
                                  "Left Outside Shoulder Width":Left_Outside_Shoulder_Width,
                                  "Left Ouside Shoulder Pavement":Left_Outside_Shoulder_Pavement,
                                   "Left Travel Way Width":Left_Travel_Way_Width,
                                   "Left Travel Way Pavement":Left_Travel_Way_Pavement,
                                   "Left Inside Shoulder Width":Left_Inside_Shoulder_Width,
                                   "Left Inside Shoulder Pavement":Left_Inside_Shoulder_Pavement,
                                   "Total Paved Width":Total_Paved_Width,
                                   "Median Width":Median_Width,
                                   "Right Travel Way Width":Right_Travel_Way_Width,
                                   "Right Travel Way Pavement":Right_Travel_Way_Pavement,
                                   "Right Ouside Shoulder Width":Right_Outside_Shoulder_Width,
                                   "Right Outside Shoulder Pavement":Right_Outside_Shoulder_Pavement,
                                   "Right Inside Shoulder Width":Right_Inside_Shoulder_Width,
                                   "Right Inside Shoulder Pavement":Right_Inside_Shoulder_Pavement,
                                   "Right Curb":Right_Curb,
                                   "Number of Through Lanes":Number_of_Through_Lanes,
                                   "On Sys Year":year_formatter(On_Sys_Year),
                                   "Rural Urban Code":Rural_Urban_Code,
                                   "System Maintenance":System_Maint,
                                   "Inventory Year":year_formatter(Inv_Year)},
        "Tiepoints":Tiepoints_Town
    }

def create_state_df(ascii_file_path):
    adict = {"Line":[],
            "Route Number":[],
            "Card Number":[],
            "Milepoint":[],
            "Road Status":[],
            "Road Class":[],
            "Town Number":[]}
    f = open(ascii_file_path,"r")
    for i in f:
        adict["Line"].append(i)
        adict["Route Number"].append(i[4:8].lstrip().rstrip())
        adict["Milepoint"].append(i[22:28])
        adict["Road Status"].append(i[21])
        adict["Road Class"].append(i[20])
        adict["Town Number"].append(i[0:3])
        adict["Card Number"].append(i[28:30])

    f.close()

    df = pd.DataFrame(adict)
    return df

def get_unique_routes_state(df):
    return df["Route Number"].unique().tolist()

def get_unique_milepoints_per_route_state(route,df):
    return df[df["Route Number"]==route]["Milepoint"].unique().tolist()

def get_top_data_state(choose_route,df):
    get_top = df[df["Route Number"]==choose_route].reset_index()
    Inventory_Month = ""
    Inventory_Year = ""
    Log_Direction = ""

    idxtop = get_top.shape[0]-1
    for i in range(get_top.shape[0]):
        if get_top.at[idxtop,"Card Number"]=="00" and len(get_top.at[idxtop,"Line"][74:76].rstrip().lstrip()) != 0:
            Inventory_Month = get_top.at[idxtop,"Line"][74:76]
            Inventory_Year = get_top.at[idxtop,"Line"][77:79]
            Log_Direction = get_top.at[idxtop,"Line"][10]
            break
        idxtop-=1
    start_index = idxtop
    return {"Log Direction":Log_Direction,
            "Inventory Month":Inventory_Month,
            "Inventory Year":year_formatter(Inventory_Year)}


def get_rest_of_data_state(choose_route,choose_milepoint,df):

    sub_df = df[df["Route Number"]==choose_route].reset_index()

    Route_Name = ""
    Town_Number = ""
    Road_Type = ""
    Road_Status = ""
    Road_Class = ""

    # go through backwards
    new_start = 0

    idx = sub_df.shape[0]-1
    for i in range(sub_df.shape[0]):
        if float(choose_milepoint) >=  float(sub_df.at[idx,"Milepoint"])and sub_df.at[idx,"Card Number"]=="00":
            Route_Name = sub_df.at[idx,"Line"][30:65].rstrip()
            Town_Number = sub_df.at[idx,"Town Number"]
            Road_Type = sub_df.at[idx,"Line"][3]
            Road_Status = sub_df.at[idx,"Road Status"]
            #Road_Class = sub_df.at[idx,"Road Class"]
            new_start=idx
            break
        idx-=1

    Latitude = ""
    Longitude = ""
    Reverse_Latitude = ""
    Reverse_Longitude = ""
    Signal_Number = ""
    # Administration
    Road_Description = ""
    Section_Length = 0
    section_length_count = False
    section_length_start_index= 0
    Nhs=""
    Fed_Aid = ""
    R_U_Designation = ""
    Functional_Class = ""
    Admin_System = ""
    Urban_Area = ""
    Reverse_Lanes = ""
    Log_Lanes = ""
    Highway_Type = ""
    Highway_Acc_Control = ""
    On_Sys_Method = ""
    On_System_Year = ""
    Adt = "" 
    Adt_Year = ""
    Adt_Break = ""
    RL_Route_Number = ""
    RL_Route_Alt = ""
    Hpms_Area = ""
    Hpms_Number = ""
    Hpms_Subdivision = ""
    Adt_Sample = ""
    Limited_Access_Report = ""
    FC_Link = ""
    Special_System_Code = ""
    #Pavement
    #Section Length From above
    Section_Length_cld = ""
    Through_Width_cld = ""
    Pavement_Type_cld = ""
    Surface_Thickness_cld = ""
    Base_Thickness_cld = ""
    Pavement_Year_cld = ""
    Improve_Type_cld = ""
    Improve_Location_cld=""
    State_Project_cld = ""
    Maint_Type_cld = ""
    Maint_Year_cld = ""
    Hpms_Median_Type_cld = ""
    Hpms_Median_Width_cld = ""
# 
    Paved_Width_clw = ""
    Pavement_Type_clw = ""
    Surface_Thickness_clw = ""
    Base_Thickness_clw=""
    Pavement_Year_clw = ""
    Improve_Type_clw = ""
    Improve_Location_clw = ""
    State_Project_clw = ""
    #Reverse Direction
    Section_Length_rd = ""
    Through_Width_rd=""
    Pavement_Type_rd = ""
    Surface_Thickness_rd = ""
    Base_Thickness_rd=""
    Pavement_Year_rd = ""
    Improve_Type_rd = ""
    Improve_Location_rd = ""
    State_Project_rd = ""
    Maint_Type_rd = ""
    Maint_Year_rd = ""
    Town_Number_rd = ""
    # Reverse widening
    Paved_Width_rw = ""
    Pavement_Type_rw = ""
    Surface_Thickness_rw = ""
    Base_Thickness_rw=""
    Pavement_Year_rw = ""
    Improve_Type_rw = ""
    Improve_Location_rw= ""
    State_Project_rw = ""
    #Pavement Configuration
    #continuous or log direction of dividend highway
    Left_Curb_c = ""
    Left_Shoulder_Width_c = ""
    Left_Shoulder_Pavement_c = ""
    Left_Aux_Type_c = ""
    Left_Aux_Lane_Width_c = ""
    Left_Aux_Lane_Pavement_c = ""
    Through_Lane_Width_c = ""
    Through_Lane_Pavement_c = ""
    Right_Aux_Type_c = ""
    Right_Aux_Lane_Width_c = ""
    Right_Aux_Lane_Pavement_c = ""
    Right_Shoulder_Width_c = ""
    Right_Shoulder_Pavement_c = ""
    Right_Curb_c = ""
    Total_Paved_Width_c = ""
    Inv_Month_c = ""
    Inv_Year_c = ""
    #reverse direction of a dividend highway 
    Left_Curb_r = ""
    Left_Shoulder_Width_r = ""
    Left_Shoulder_Pavement_r = ""
    Left_Aux_Type_r = ""
    Left_Aux_Lane_Width_r = ""
    Left_Aux_Lane_Pavement_r = ""
    Through_Lane_Width_r = ""
    Through_Lane_Pavement_r = ""
    Right_Aux_Type_r = ""
    Right_Aux_Lane_Width_r = ""
    Right_Aux_Lane_Pavement_r = ""
    Right_Shoulder_Width_r = ""
    Right_Shoulder_Pavement_r = ""
    Right_Curb_r = ""
    Median_Type_r = ""
    Median_Width_r = ""
    #Tiepoints
    Tiepoints_State = {}
    for i in range(new_start+1,sub_df.shape[0]):
        line = sub_df.at[i,"Line"]
    
        if sub_df.at[i,"Card Number"]=="00":
            break
        if sub_df.at[i,"Card Number"] == "10" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Latitude = line[43:52]
            Longitude = line[53:62]
            Reverse_Latitude = line[62:71]
            Reverse_Longitude = line[72:81]
            Road_Class = sub_df.at[i,"Road Class"]
        if "SIGNAL #" in sub_df.at[i,"Line"] and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Signal_Number = sub_df.at[i,"Line"].split("# ")[-1].replace("\n","")
        if sub_df.at[i,"Card Number"]=="02" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Road_Description = sub_df.at[i,"Line"][30:65]
            try:
                RL_Route_Number = sub_df.at[i,"Line"][72:75]
            except IndexError:
                pass
            try:
                RL_Route_Alt = sub_df.at[i,"Line"][75]
            except IndexError:
                pass
           # Section_Length = float(sub_df.at[i,"Milepoint"][:3]+'.'+sub_df.at[i,"Milepoint"][3:])
            #section_length_count = True
        if sub_df.at[i,"Card Number"]=="11" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            try:
                
                Section_Length = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
                section_length_count = True
            except ValueError:
                pass
            Road_Class = sub_df.at[i,"Road Class"]
            # go back here
           # Section_Length=float(sub_df.at[i,"Milepoint"][:3]+'.'+sub_df.at[i,"Milepoint"][3:])-Section_Length
           # section_length_count=False
        if sub_df.at[i,"Card Number"]=="01" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            section_length_start_index = i 
            Nhs = sub_df.at[i,"Line"][30]
            Fed_Aid = sub_df.at[i,"Line"][32]
            R_U_Designation = sub_df.at[i,"Line"][31]
            Admin_System = sub_df.at[i,"Line"][33]
            Urban_Area = sub_df.at[i,"Line"][38]
            Reverse_Lanes = sub_df.at[i,"Line"][59]
            Log_Lanes = sub_df.at[i,"Line"][60]
            Highway_Type = sub_df.at[i,"Line"][62]
            Highway_Acc_Control=sub_df.at[i,"Line"][64]
            On_Sys_Method = sub_df.at[i,"Line"][66]
            On_System_Year = sub_df.at[i,"Line"][67:71]
            Adt = sub_df.at[i,"Line"][73:79]
            Adt_Year = sub_df.at[i,"Line"][71:73]
            Road_Class = sub_df.at[i,"Road Class"]
            try:
                Limited_Access_Report = sub_df.at[i,"Line"][80]
            except IndexError:
                pass
            Special_System_Code = sub_df.at[i,"Line"][40]
        if sub_df.at[i,"Card Number"]=="03" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Functional_Class = sub_df.at[i,"Line"][65:67]
            Hpms_Area = sub_df.at[i,"Line"][44]
            Hpms_Number = sub_df.at[i,"Line"][45:48]
            Hpms_Subdivision = sub_df.at[i,"Line"][48]
            Adt_Sample = sub_df.at[i,"Line"][49]
            FC_Link = sub_df.at[i,"Line"][67]
            Road_Class = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="32" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            try:
                Adt_Break = sub_df.at[i,"Line"][83]
            except IndexError:
                pass
        if (sub_df.at[i,"Card Number"]=="14" or sub_df.at[i,"Card Number"]=="11") and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Through_Width_cld = sub_df.at[i,"Line"][38:41]
            Pavement_Type_cld = sub_df.at[i,"Line"][41:45]
            Surface_Thickness_cld = sub_df.at[i,"Line"][45]
            Base_Thickness_cld = sub_df.at[i,"Line"][46]
            Pavement_Year_cld = sub_df.at[i,"Line"][47:49]
            Improve_Type_cld=sub_df.at[i,"Line"][49]
            Improve_Location_cld=sub_df.at[i,"Line"][50]
            State_Project_cld = sub_df.at[i,"Line"][54:60]
            Maint_Type_cld = sub_df.at[i,"Line"][60]
            Maint_Year_cld = sub_df.at[i,"Line"][61:63]
            Road_Class = sub_df.at[i,"Road Class"]
            try:
                
                Section_Length_cld = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
            except ValueError:
                pass
            try:
                Hpms_Median_Type_cld=sub_df.at[i,"Line"][66]
            except IndexError:
                pass
            try:
                Hpms_Median_Width_cld=sub_df.at[i,"Line"][67:70]
            except IndexError:
                pass
        if (sub_df.at[i,"Card Number"]=="15" or sub_df.at[i,"Card Number"]=="12") and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Paved_Width_clw=sub_df.at[i,"Line"][38:41]
            Pavement_Type_clw=sub_df.at[i,"Line"][41:45]
            Surface_Thickness_clw = sub_df.at[i,"Line"][45]
            Base_Thickness_clw = sub_df.at[i,"Line"][46]
            Pavement_Year_clw = sub_df.at[i,"Line"][47:49]
            Improve_Type_clw=sub_df.at[i,"Line"][49]
            Improve_Location_clw=sub_df.at[i,"Line"][50]
            State_Project_clw = sub_df.at[i,"Line"][54:60]
            Road_Class = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="17" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Section_Length_rd = sub_df.at[i,"Line"][30:35]
            Through_Width_rd = sub_df.at[i,"Line"][38:41]
            Pavement_Type_rd = sub_df.at[i,"Line"][41:45]
            Surface_Thickness_rd = sub_df.at[i,"Line"][45]
            Base_Thickness_rd = sub_df.at[i,"Line"][46]
            Pavement_Year_rd = sub_df.at[i,"Line"][47:49]
            Improve_Type_rd=sub_df.at[i,"Line"][49]
            Improve_Location_rd=sub_df.at[i,"Line"][50]
            State_Project_rd = sub_df.at[i,"Line"][54:60]
            Maint_Type_rd = sub_df.at[i,"Line"][60]
            Maint_Year_rd = sub_df.at[i,"Line"][61:63]
            Town_Number_rd = sub_df.at[i,"Line"][70:73]
            Road_Class = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="18" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Paved_Width_rw=sub_df.at[i,"Line"][38:41]
            Pavement_Type_rw=sub_df.at[i,"Line"][41:45]
            Surface_Thickness_rw = sub_df.at[i,"Line"][45]
            Base_Thickness_rw = sub_df.at[i,"Line"][46]
            Pavement_Year_rw = sub_df.at[i,"Line"][47:49]
            Improve_Type_rw=sub_df.at[i,"Line"][49]
            Improve_Location_rw=sub_df.at[i,"Line"][50]
            State_Project_rw = sub_df.at[i,"Line"][54:60]
            Road_Class = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="30" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb_c = sub_df.at[i,"Line"][30]
            Left_Shoulder_Width_c = sub_df.at[i,"Line"][31:33]
            Left_Shoulder_Pavement_c = sub_df.at[i,"Line"][33:35]
            Left_Aux_Type_c = sub_df.at[i,"Line"][35]
            Left_Aux_Lane_Width_c = sub_df.at[i,"Line"][36:38]
            Left_Aux_Lane_Pavement_c = sub_df.at[i,"Line"][38:40]
            Through_Lane_Width_c = sub_df.at[i,"Line"][40:42]
            Through_Lane_Pavement_c = sub_df.at[i,"Line"][42:44]
            Right_Aux_Type_c = sub_df.at[i,"Line"][44]
            Right_Aux_Lane_Width_c = sub_df.at[i,"Line"][45:47]
            Right_Aux_Lane_Pavement_c = sub_df.at[i,"Line"][47:49]
            Right_Shoulder_Width_c=sub_df.at[i,"Line"][49:51]
            Right_Shoulder_Pavement_c = sub_df.at[i,"Line"][51:53]
            Right_Curb_c = sub_df.at[i,"Line"][53]
            Total_Paved_Width_c = sub_df.at[i,"Line"][54:57]
            Inv_Month_c =sub_df.at[i,"Line"][57:59]
            Inv_Year_c = sub_df.at[i,"Line"][59:61]
            Road_Class = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="31" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb_r = sub_df.at[i,"Line"][30]
            Left_Shoulder_Width_r = sub_df.at[i,"Line"][31:33]
            Left_Shoulder_Pavement_r = sub_df.at[i,"Line"][33:35]
            Left_Aux_Type_r = sub_df.at[i,"Line"][35]
            Left_Aux_Lane_Width_r = sub_df.at[i,"Line"][36:38]
            Left_Aux_Lane_Pavement_r = sub_df.at[i,"Line"][38:40]
            Through_Lane_Width_r = sub_df.at[i,"Line"][40:42]
            Through_Lane_Pavement_r = sub_df.at[i,"Line"][42:44]
            Right_Aux_Type_r = sub_df.at[i,"Line"][44]
            Right_Aux_Lane_Width_r = sub_df.at[i,"Line"][45:47]
            Right_Aux_Lane_Pavement_r = sub_df.at[i,"Line"][47:49]
            Right_Shoulder_Width_r=sub_df.at[i,"Line"][49:51]
            Right_Shoulder_Pavement_r = sub_df.at[i,"Line"][51:53]
            Right_Curb_r = sub_df.at[i,"Line"][53]
            Median_Type_r = sub_df.at[i,"Line"][54]
            Median_Width_r = sub_df.at[i,"Line"][55:58]
            Road_Class = sub_df.at[i,"Road Class"]
        if int(sub_df.at[i,"Card Number"]) >= 32 and int(sub_df.at[i,"Card Number"]) <=48 and int(sub_df.at[i,"Card Number"]) %2 == 0 and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Road_Class = sub_df.at[i,"Road Class"]
            Intersection_Description = sub_df.at[i,"Line"][30:65].rstrip()
            Intersection_Route = ""
            Intersection_Road = ""
            Tiepoint_Type = ""
            Tiepoint_Code = ""
            Bridge_Prefix = ""
            Bridge_Suffix = ""
            Bridge_Number = ""
            One_Way = ""
            Angle = ""
            Road_Class_d=""
            Intersecting_Town = ""
            Suffix = ""
            Ramp_Or_Tr_num=""
            try:
                Angle = sub_df.at[i+1,"Line"][52:54]
            except IndexError:
                pass
            try:
                Bridge_Suffix = sub_df.at[i,"Line"][71]
            except IndexError:
                pass
            try:
                Bridge_Number = sub_df.at[i,"Line"][66:71]
            except IndexError:
                pass
            try:
                Bridge_Prefix = sub_df.at[i,"Line"][65]
            except IndexError:
                pass
            try:
                Tiepoint_Type = sub_df.at[i,"Line"][72]
            except IndexError:
                pass
            try:
                One_Way = sub_df.at[i+1,"Line"][54]
            except IndexError:
                pass
            try:
                Road_Class_d = sub_df.at[i+1,"Line"][50]
            except IndexError:
                pass
            try:
                Intersecting_Town = sub_df.at[i+1,"Line"][30:33]
            except IndexError:
                pass
            try:
                Suffix = sub_df.at[i+1,"Line"][47]
            except IndexError:
                pass
            try:
                Ramp_Or_Tr_num = sub_df.at[i+1,"Line"][44:47]
            except IndexError:
                pass

            if sub_df.at[i+1,"Line"][30:33]==Town_Number and sub_df.at[i+1,"Line"][33] != "9":
                if "A" in sub_df.at[i+1,"Line"][31:36] or "E" in sub_df.at[i+1,"Line"][31:36]:
                    Intersection_Route = sub_df.at[i+1,"Line"][34:38]
                else:
                    Intersection_Road = sub_df.at[i+1,"Line"][33:37]
            Tiepoint_Code = ""
            if "A" not in sub_df.at[i+1,"Line"][31:36]:
                if "SIGNAL #" in Intersection_Description:
                    Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
                else:
                    if sub_df.at[i+1,"Line"][30:33]==sub_df.at[i,"Line"][0:3] and sub_df.at[i+1,"Line"][33] == "9":
                        Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
            Bridge_Location = ""
            try:
                if sub_df.at[i,"Line"][72]=="A":
                    Bridge_Location = sub_df.at[i,"Line"][73]
            except IndexError:
                pass
            Exit_Number = ""
            Exit_Suffix = ""
            try:
                if sub_df.at[i,"Line"][72]=="X":
                    Exit_Number = sub_df.at[i,"Line"][73:77]
                    Exit_Suffix = sub_df.at[i,"Line"][77]
            except IndexError:
                pass
            Pole_Number=""
            tiepoint_type_poles = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
            try:
                if sub_df.at[i,"Line"][72] in tiepoint_type_poles:
                    Pole_Number = sub_df.at[i,"Line"][73:79]
            except IndexError:
                pass
            RR_Crossing_Number = ""
            tiepoint_type_RR = ["1","2","3","4","5","6","7","8","9"]
            try:
                if sub_df.at[i,"Line"][72] in tiepoint_type_RR:
                    RR_Crossing_Number = sub_df.at[i,"Line"][73:79]
            except IndexError:
                pass
            Connector = ""
            Connector_Seq = ""
            try:
                if sub_df.at[i+1,"Line"][37]=="C":
                    Connector = "C"
                    Connector_Seq = sub_df.at[i+1,"Line"][38:40]
            except IndexError:
                pass
            try:
                if sub_df.at[i+1,"Line"][37] != "C":
                    try:
                        if sub_df.at[i+2,"Card Number"]=="32" and sub_df.at[i+3,"Line"][37]=="C":
                            Connector = "C"
                    except (IndexError,KeyError):
                        pass
            except IndexError:
                pass
        
            if Intersection_Description in Tiepoints_State:
                for i in range(1,100):
                    if Intersection_Description +"_"+str(i) not in Tiepoints_State:
                        Intersection_Description = Intersection_Description + "_"+str(i)
                        break
            Interchange = ""
            adt_break = ""
            Hw_Log_Codes = ""
            try:
                Interchange = sub_df.at[i,"Line"][82]
            except IndexError:
                Interchange = ""
            try:
                adt_break = sub_df.at[i,"Line"][83]
            except IndexError:
                adt_break = ""
            try:
                Hw_Log_Codes = sub_df.at[i,"Line"][80:82]
            except IndexError:
                Hw_Log_Codes = ""


            Tiepoints_State[Intersection_Description] = {"Intersection Route":Intersection_Route,
                                                    "Ramp or TR #":Ramp_Or_Tr_num,
                                                    "Suffix":Suffix,
                                                    "Intersecting Town":Intersecting_Town,
                                                    "Intersecting Road":Intersection_Road,
                                                    "Road Class":Road_Class_d,
                                                    "Connector":Connector,
                                                    "Connector Seq.":Connector_Seq,
                                                    "One Way":One_Way,
                                                    "Tiepoint Code":Tiepoint_Code,
                                                    "Tiepoint Type":Tiepoint_Type,
                                                    "Bridge Prefix":Bridge_Prefix,
                                                    "Bridge Number":Bridge_Number,
                                                    "Bridge Suffix":Bridge_Suffix,
                                                    "Bridge Location":Bridge_Location,
                                                    "Exit #":Exit_Number,
                                                    "Exit Suffix":Exit_Suffix,
                                                    "Pole #":Pole_Number,
                                                    "Interchange":Interchange,
                                                    "RR Crossing #":RR_Crossing_Number,
                                                    "ADT Break":adt_break,
                                                    "Angle":Angle,
                                                    "HW Log Codes":Hw_Log_Codes.replace("\n","")

                                                    }
    
    
    if not section_length_count:
        for i in range(new_start+1,sub_df.shape[0]):
            if sub_df.at[i,"Card Number"]=="14" and choose_milepoint == sub_df.at[i,"Milepoint"]:
                try:
                
                    Section_Length = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
            
                except ValueError:
                    pass


       

    return {"Top":{"Route Name":Route_Name,
                        "Town Number":Town_Number,
                        "Road Type":Road_Type,
                        "Road Class":Road_Class,
                        "Signal Number":Signal_Number,
                        "Road Status":Road_Status,
                        "Latitude":Latitude,
                        "Longitude":Longitude,
                        "Reverse Latitude":Reverse_Latitude,
                        "Reverse Longitude":Reverse_Longitude},
                "Administration":{"Road Description":Road_Description.rstrip(),
                                  "Section Length":Section_Length,
                                  "NHS":Nhs,
                                  "Fed Aid":Fed_Aid,
                                  "R/U Designation":R_U_Designation,
                                  "Functional Class":Functional_Class,
                                  "Admin System":Admin_System,
                                  "Urban Area":Urban_Area,
                                  "Reverse Lanes":Reverse_Lanes,
                                  "Log Lanes":Log_Lanes,
                                  "Highway Type":Highway_Type,
                                  "Highway Acc. Ctrl.":Highway_Acc_Control,
                                  "On Sys Method":On_Sys_Method,
                                  "On System Year":year_formatter(On_System_Year),
                                  "ADT":Adt,
                                  "ADT Year":year_formatter(Adt_Year),
                                  "ADT Break":Adt_Break,
                                  "RL Route #":RL_Route_Number,
                                  "RL Rte. Alternative":RL_Route_Alt,
                                  "HPMS Area":Hpms_Area,
                                  "HPMS Number":Hpms_Number,
                                  "HPMS Subdivision":Hpms_Subdivision,
                                  "ADT Sample":Adt_Sample,
                                  "LIM Access Report":Limited_Access_Report,
                                  "FC Link":FC_Link,
                                  "Special System Code":Special_System_Code},
                "Pavement":{"cont or log dir":{"Section Length":Section_Length_cld,
                                                "Through Width":Through_Width_cld,
                                                "Pavement Type":Pavement_Type_cld,
                                                "Surface Thickness":Surface_Thickness_cld,
                                                "Base Thickness":Base_Thickness_cld,
                                                "Pavement Year":year_formatter(Pavement_Year_cld),
                                                "Improve Type":Improve_Type_cld,
                                                "Improve Loc":Improve_Location_cld,
                                                "State Project":State_Project_cld,
                                                "Maint Type":Maint_Type_cld,
                                                "Maint Year":year_formatter(Maint_Year_cld),
                                                "HPMS Median Type":Hpms_Median_Type_cld,
                                                "HPMS Median Width":Hpms_Median_Width_cld},
                            "cont or log wid":{"Paved Width":Paved_Width_clw,
                                                "Pavement Type":Pavement_Type_clw,
                                                "Surface Thickness":Surface_Thickness_clw,
                                                "Base Thickness":Base_Thickness_clw,
                                                "Pavement Year":year_formatter(Pavement_Year_clw),
                                                "Improve Type":Improve_Type_clw,
                                                "Improve Loc":Improve_Location_clw,
                                                "State Project":State_Project_clw},
                            "reverse direction":{"Section Length":Section_Length_rd,
                                                "Through Width":Through_Width_rd,
                                                "Pavement Type":Pavement_Type_rd,
                                                "Surface Thickness":Surface_Thickness_rd,
                                                "Base Thickness":Base_Thickness_rd,
                                                "Pavement Year":year_formatter(Pavement_Year_rd),
                                                "Improve Type":Improve_Type_rd,
                                                "Improve Loc":Improve_Location_rd,
                                                "State Project":State_Project_rd,
                                                "Maint Type":Maint_Type_rd,
                                                "Maint Year":year_formatter(Maint_Year_rd),
                                                "Town # rev. Direction":Town_Number_rd},
                            "reverse widening":{"Paved Width":Paved_Width_rw,
                                                "Pavement Type":Pavement_Type_rw,
                                                "Surface Thickness":Surface_Thickness_rw,
                                                "Base Thickness":Base_Thickness_rw,
                                                "Pavement Year":year_formatter(Pavement_Year_rw),
                                                "Improve Type":Improve_Type_rw,
                                                "Improve Loc":Improve_Location_rw,
                                                "State Project":State_Project_rw}},
                "Pavement Configuration":{"cont or log dir":{"Left Curb":Left_Curb_c,
                                                            "Left Shoulder Width":Left_Shoulder_Width_c,
                                                            "Left Shoulder Pavement":Left_Shoulder_Pavement_c,
                                                            "Left Aux Lane Type":Left_Aux_Type_c,
                                                            "Left Aux Lane Width":Left_Aux_Lane_Width_c,
                                                            "Left Aux Lane Pavement":Left_Aux_Lane_Pavement_c,
                                                            "Through Lane Width":Through_Lane_Width_c,
                                                            "Through Lane Pavement":Through_Lane_Pavement_c,
                                                            "Right Aux Lane Type":Right_Aux_Type_c,
                                                            "Right Aux Lane Width":Right_Aux_Lane_Width_c,
                                                            "Right Aux Lane Pavement":Right_Aux_Lane_Pavement_c,
                                                            "Right Shoulder Width":Right_Shoulder_Width_c,
                                                            "Right Shoulder Pavement":Right_Shoulder_Pavement_c,
                                                            "Right Curb":Right_Curb_c,
                                                            "Total Paved Width":Total_Paved_Width_c,
                                                            "Inventory Month":Inv_Month_c,
                                                            "Inventory Year":year_formatter(Inv_Year_c)},
                                            "rev dir div":{"Left Curb":Left_Curb_r,
                                                            "Left Shoulder Width":Left_Shoulder_Width_r,
                                                            "Left Shoulder Pavement":Left_Shoulder_Pavement_r,
                                                            "Left Aux Lane Type":Left_Aux_Type_r,
                                                            "Left Aux Lane Width":Left_Aux_Lane_Width_r,
                                                            "Left Aux Lane Pavement":Left_Aux_Lane_Pavement_r,
                                                            "Through Lane Width":Through_Lane_Width_r,
                                                            "Through Lane Pavement":Through_Lane_Pavement_r,
                                                            "Right Aux Lane Type":Right_Aux_Type_r,
                                                            "Right Aux Lane Width":Right_Aux_Lane_Width_r,
                                                            "Right Aux Lane Pavement":Right_Aux_Lane_Pavement_r,
                                                            "Right Shoulder Width":Right_Shoulder_Width_r,
                                                            "Right Shoulder Pavement":Right_Shoulder_Pavement_r,
                                                            "Right Curb":Right_Curb_r,
                                                            "Median Type":Median_Type_r,
                                                            "Median Width":Median_Width_r}},
                "Tiepoints":Tiepoints_State}


#######################################################################################################################################

def create_sis_df(ascii_file_path):
    adict = {"Line":[],
            "Route Number":[],
            "Card Number":[],
            "Milepoint":[],
            "Road Status":[],
            "Road Class":[],
            "Town Number":[]}
    f = open(ascii_file_path,"r")
    for i in f:
        adict["Line"].append(i)
        adict["Route Number"].append(i[4:8].lstrip().rstrip())
        adict["Milepoint"].append(i[22:28])
        adict["Road Status"].append(i[21])
        adict["Road Class"].append(i[20])
        adict["Town Number"].append(i[0:3])
        adict["Card Number"].append(i[28:30])

    f.close()

    df = pd.DataFrame(adict)
    return df

def get_unique_routes_sis(df):
    return df["Route Number"].unique().tolist()

def get_unique_milepoints_per_route_sis(route,df):
    return df[df["Route Number"]==route]["Milepoint"].unique().tolist()

def get_top_data_sis(choose_route,df):
    get_top = df[df["Route Number"]==choose_route].reset_index()
    Inventory_Month = ""
    Inventory_Year = ""
    Log_Direction = ""

    idxtop = get_top.shape[0]-1
    for i in range(get_top.shape[0]):
        if get_top.at[idxtop,"Card Number"]=="00" and len(get_top.at[idxtop,"Line"][74:76].rstrip().lstrip()) != 0:
            Inventory_Month = get_top.at[idxtop,"Line"][74:76]
            Inventory_Year = get_top.at[idxtop,"Line"][77:79]
            Log_Direction = get_top.at[idxtop,"Line"][10]
            break
        idxtop-=1
    start_index = idxtop
    return {"Log Direction":Log_Direction,
            "Inventory Month":Inventory_Month,
            "Inventory Year":year_formatter(Inventory_Year)}


def get_rest_of_data_sis(choose_route,choose_milepoint,df):

    sub_df = df[df["Route Number"]==choose_route].reset_index()

    Route_Name = ""
    Town_Number = ""
    Road_Type = ""
    Road_Status = ""
    Road_Class_top = ""

    # go through backwards
    new_start = 0

    idx = sub_df.shape[0]-1
    for i in range(sub_df.shape[0]):
        if float(choose_milepoint) >=  float(sub_df.at[idx,"Milepoint"])and sub_df.at[idx,"Card Number"]=="00":
            Route_Name = sub_df.at[idx,"Line"][30:65].rstrip()
            Town_Number = sub_df.at[idx,"Town Number"]
            Road_Type = sub_df.at[idx,"Line"][3]
            Road_Status = sub_df.at[idx,"Road Status"]
            #Road_Class_top = sub_df.at[idx,"Road Class"]
            new_start=idx
            break
        idx-=1

    Latitude = ""
    Longitude = ""
    Reverse_Latitude = ""
    Reverse_Longitude = ""
    Signal_Number = ""
    # Administration
    Road_Description = ""
    Section_Length = 0
    section_length_count = False
    section_length_start_index= 0
    
    Nhs=""
    Fed_Aid = ""
    R_U_Designation = ""
    Functional_Class = ""
    Admin_System = ""
    Urban_Area = ""
    Reverse_Lanes = ""
    Log_Lanes = ""
    Highway_Type = ""
    Highway_Acc_Control = ""
    On_Sys_Method = ""
    On_System_Year = ""
    Adt = "" 
    Adt_Year = ""
    Adt_Break = ""
    RL_Route_Number = ""
    RL_Route_Alt = ""
    Hpms_Area = ""
    Hpms_Number = ""
    Hpms_Subdivision = ""
    Adt_Sample = ""
    Limited_Access_Report = ""
    FC_Link = ""
    Special_System_Code = ""
    #Pavement
    #Section Length From above
    Section_Length_cld = ""
    Through_Width_cld = ""
    Pavement_Type_cld = ""
    Surface_Thickness_cld = ""
    Base_Thickness_cld = ""
    Pavement_Year_cld = ""
    Improve_Type_cld = ""
    Improve_Location_cld=""
    State_Project_cld = ""
    Maint_Type_cld = ""
    Maint_Year_cld = ""
    Hpms_Median_Type_cld = ""
    Hpms_Median_Width_cld = ""
# 
    Paved_Width_clw = ""
    Pavement_Type_clw = ""
    Surface_Thickness_clw = ""
    Base_Thickness_clw=""
    Pavement_Year_clw = ""
    Improve_Type_clw = ""
    Improve_Location_clw = ""
    State_Project_clw = ""
    #Reverse Direction
    Section_Length_rd = ""
    Through_Width_rd=""
    Pavement_Type_rd = ""
    Surface_Thickness_rd = ""
    Base_Thickness_rd=""
    Pavement_Year_rd = ""
    Improve_Type_rd = ""
    Improve_Location_rd = ""
    State_Project_rd = ""
    Maint_Type_rd = ""
    Maint_Year_rd = ""
    Town_Number_rd = ""
    # Reverse widening
    Paved_Width_rw = ""
    Pavement_Type_rw = ""
    Surface_Thickness_rw = ""
    Base_Thickness_rw=""
    Pavement_Year_rw = ""
    Improve_Type_rw = ""
    Improve_Location_rw= ""
    State_Project_rw = ""
    #Pavement Configuration
    #continuous or log direction of dividend highway
    Left_Curb_c = ""
    Left_Shoulder_Width_c = ""
    Left_Shoulder_Pavement_c = ""
    Left_Aux_Type_c = ""
    Left_Aux_Lane_Width_c = ""
    Left_Aux_Lane_Pavement_c = ""
    Through_Lane_Width_c = ""
    Through_Lane_Pavement_c = ""
    Right_Aux_Type_c = ""
    Right_Aux_Lane_Width_c = ""
    Right_Aux_Lane_Pavement_c = ""
    Right_Shoulder_Width_c = ""
    Right_Shoulder_Pavement_c = ""
    Right_Curb_c = ""
    Total_Paved_Width_c = ""
    Inv_Month_c = ""
    Inv_Year_c = ""
    #reverse direction of a dividend highway 
    Left_Curb_r = ""
    Left_Shoulder_Width_r = ""
    Left_Shoulder_Pavement_r = ""
    Left_Aux_Type_r = ""
    Left_Aux_Lane_Width_r = ""
    Left_Aux_Lane_Pavement_r = ""
    Through_Lane_Width_r = ""
    Through_Lane_Pavement_r = ""
    Right_Aux_Type_r = ""
    Right_Aux_Lane_Width_r = ""
    Right_Aux_Lane_Pavement_r = ""
    Right_Shoulder_Width_r = ""
    Right_Shoulder_Pavement_r = ""
    Right_Curb_r = ""
    Median_Type_r = ""
    Median_Width_r = ""
    #Tiepoints
    Tiepoints_State = {}
    for i in range(new_start+1,sub_df.shape[0]):
        line = sub_df.at[i,"Line"]
    
        if sub_df.at[i,"Card Number"]=="00":
            break
        if sub_df.at[i,"Card Number"] == "10" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Latitude = line[43:52]
            Longitude = line[53:62]
            Reverse_Latitude = line[62:71]
            Reverse_Longitude = line[72:81]
        if "SIGNAL #" in sub_df.at[i,"Line"] and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Signal_Number = sub_df.at[i,"Line"].split("# ")[-1].replace("\n","")
        if sub_df.at[i,"Card Number"]=="02" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Road_Description = sub_df.at[i,"Line"][30:65]
            RL_Route_Number = sub_df.at[i,"Line"][72:75]
            try:
                RL_Route_Alt = sub_df.at[i,"Line"][75]
            except IndexError:
                pass
        if sub_df.at[i,"Card Number"]=="11" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            try:
                
                Section_Length = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
                section_length_count = True
            except ValueError:
                pass
        if sub_df.at[i,"Card Number"]=="01" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            section_length_start_index=i
            Nhs = sub_df.at[i,"Line"][30]
            Fed_Aid = sub_df.at[i,"Line"][32]
            R_U_Designation = sub_df.at[i,"Line"][31]
            Admin_System = sub_df.at[i,"Line"][33]
            Urban_Area = sub_df.at[i,"Line"][38]
            Reverse_Lanes = sub_df.at[i,"Line"][59]
            Log_Lanes = sub_df.at[i,"Line"][60]
            Highway_Type = sub_df.at[i,"Line"][62]
            Highway_Acc_Control=sub_df.at[i,"Line"][64]
            On_Sys_Method = sub_df.at[i,"Line"][66]
            On_System_Year = sub_df.at[i,"Line"][67:71]
            Adt = sub_df.at[i,"Line"][73:79]
            Adt_Year = sub_df.at[i,"Line"][71:73]
            Road_Class_top = sub_df.at[i,"Road Class"]
            try:
                Limited_Access_Report = sub_df.at[i,"Line"][80]
            except IndexError:
                pass
            Special_System_Code = sub_df.at[i,"Line"][40]
        if sub_df.at[i,"Card Number"]=="03" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Functional_Class = sub_df.at[i,"Line"][65:67]
            Hpms_Area = sub_df.at[i,"Line"][44]
            Hpms_Number = sub_df.at[i,"Line"][45:48]
            Hpms_Subdivision = sub_df.at[i,"Line"][48]
            Adt_Sample = sub_df.at[i,"Line"][49]
            FC_Link = sub_df.at[i,"Line"][67]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="32" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            try:
                Adt_Break = sub_df.at[i,"Line"][83]
            except IndexError:
                pass
        if (sub_df.at[i,"Card Number"]=="14" or sub_df.at[i,"Card Number"]=="11") and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Through_Width_cld = sub_df.at[i,"Line"][38:41]
            Pavement_Type_cld = sub_df.at[i,"Line"][41:45]
            Surface_Thickness_cld = sub_df.at[i,"Line"][45]
            Base_Thickness_cld = sub_df.at[i,"Line"][46]
            Pavement_Year_cld = sub_df.at[i,"Line"][47:49]
            Improve_Type_cld=sub_df.at[i,"Line"][49]
            Improve_Location_cld=sub_df.at[i,"Line"][50]
            State_Project_cld = sub_df.at[i,"Line"][54:60]
            Maint_Type_cld = sub_df.at[i,"Line"][60]
            Maint_Year_cld = sub_df.at[i,"Line"][61:63]
            Hpms_Median_Type_cld=sub_df.at[i,"Line"][66]
            Hpms_Median_Width_cld=sub_df.at[i,"Line"][67:70]
            try:
                
                Section_Length_cld = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
            except ValueError:
                pass
            Road_Class_top = sub_df.at[i,"Road Class"]
        if (sub_df.at[i,"Card Number"]=="15" or sub_df.at[i,"Card Number"]=="12") and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Paved_Width_clw=sub_df.at[i,"Line"][38:41]
            Pavement_Type_clw=sub_df.at[i,"Line"][41:45]
            Surface_Thickness_clw = sub_df.at[i,"Line"][45]
            Base_Thickness_clw = sub_df.at[i,"Line"][46]
            Pavement_Year_clw = sub_df.at[i,"Line"][47:49]
            Improve_Type_clw=sub_df.at[i,"Line"][49]
            Improve_Location_clw=sub_df.at[i,"Line"][50]
            State_Project_clw = sub_df.at[i,"Line"][54:60]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="17" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Section_Length_rd = sub_df.at[i,"Line"][30:35]
            Through_Width_rd = sub_df.at[i,"Line"][38:41]
            Pavement_Type_rd = sub_df.at[i,"Line"][41:45]
            Surface_Thickness_rd = sub_df.at[i,"Line"][45]
            Base_Thickness_rd = sub_df.at[i,"Line"][46]
            Pavement_Year_rd = sub_df.at[i,"Line"][47:49]
            Improve_Type_rd=sub_df.at[i,"Line"][49]
            Improve_Location_rd=sub_df.at[i,"Line"][50]
            State_Project_rd = sub_df.at[i,"Line"][54:60]
            Maint_Type_rd = sub_df.at[i,"Line"][60]
            Maint_Year_rd = sub_df.at[i,"Line"][61:63]
            Town_Number_rd = sub_df.at[i,"Line"][70:73]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="18" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Paved_Width_rw=sub_df.at[i,"Line"][38:41]
            Pavement_Type_rw=sub_df.at[i,"Line"][41:45]
            Surface_Thickness_rw = sub_df.at[i,"Line"][45]
            Base_Thickness_rw = sub_df.at[i,"Line"][46]
            Pavement_Year_rw = sub_df.at[i,"Line"][47:49]
            Improve_Type_rw=sub_df.at[i,"Line"][49]
            Improve_Location_rw=sub_df.at[i,"Line"][50]
            State_Project_rw = sub_df.at[i,"Line"][54:60]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="30" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb_c = sub_df.at[i,"Line"][30]
            Left_Shoulder_Width_c = sub_df.at[i,"Line"][31:33]
            Left_Shoulder_Pavement_c = sub_df.at[i,"Line"][33:35]
            Left_Aux_Type_c = sub_df.at[i,"Line"][35]
            Left_Aux_Lane_Width_c = sub_df.at[i,"Line"][36:38]
            Left_Aux_Lane_Pavement_c = sub_df.at[i,"Line"][38:40]
            Through_Lane_Width_c = sub_df.at[i,"Line"][40:42]
            Through_Lane_Pavement_c = sub_df.at[i,"Line"][42:44]
            Right_Aux_Type_c = sub_df.at[i,"Line"][44]
            Right_Aux_Lane_Width_c = sub_df.at[i,"Line"][45:47]
            Right_Aux_Lane_Pavement_c = sub_df.at[i,"Line"][47:49]
            Right_Shoulder_Width_c=sub_df.at[i,"Line"][49:51]
            Right_Shoulder_Pavement_c = sub_df.at[i,"Line"][51:53]
            Right_Curb_c = sub_df.at[i,"Line"][53]
            Total_Paved_Width_c = sub_df.at[i,"Line"][54:57]
            Inv_Month_c =sub_df.at[i,"Line"][57:59]
            Inv_Year_c = sub_df.at[i,"Line"][59:61]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if sub_df.at[i,"Card Number"]=="31" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb_r = sub_df.at[i,"Line"][30]
            Left_Shoulder_Width_r = sub_df.at[i,"Line"][31:33]
            Left_Shoulder_Pavement_r = sub_df.at[i,"Line"][33:35]
            Left_Aux_Type_r = sub_df.at[i,"Line"][35]
            Left_Aux_Lane_Width_r = sub_df.at[i,"Line"][36:38]
            Left_Aux_Lane_Pavement_r = sub_df.at[i,"Line"][38:40]
            Through_Lane_Width_r = sub_df.at[i,"Line"][40:42]
            Through_Lane_Pavement_r = sub_df.at[i,"Line"][42:44]
            Right_Aux_Type_r = sub_df.at[i,"Line"][44]
            Right_Aux_Lane_Width_r = sub_df.at[i,"Line"][45:47]
            Right_Aux_Lane_Pavement_r = sub_df.at[i,"Line"][47:49]
            Right_Shoulder_Width_r=sub_df.at[i,"Line"][49:51]
            Right_Shoulder_Pavement_r = sub_df.at[i,"Line"][51:53]
            Right_Curb_r = sub_df.at[i,"Line"][53]
            Median_Type_r = sub_df.at[i,"Line"][54]
            Median_Width_r = sub_df.at[i,"Line"][55:58]
            Road_Class_top = sub_df.at[i,"Road Class"]
        if int(sub_df.at[i,"Card Number"]) >= 32 and int(sub_df.at[i,"Card Number"]) <=48 and int(sub_df.at[i,"Card Number"]) %2 == 0 and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Intersection_Description = sub_df.at[i,"Line"][30:65].rstrip()
            Intersection_Route = ""
            Intersection_Road = ""
            Angle = sub_df.at[i+1,"Line"][52:54]
            Bridge_Suffix = sub_df.at[i,"Line"][71]
            Bridge_Number = sub_df.at[i,"Line"][66:71]
            Highway_Log_Codes = sub_df.at[i,"Line"][80:82]
            Bridge_Prefix = sub_df.at[i,"Line"][65]
            Tiepoint_Type = sub_df.at[i,"Line"][72]
            One_Way = sub_df.at[i+1,"Line"][54]
            Road_Class = sub_df.at[i+1,"Line"][50]
            Intersecting_Town = sub_df.at[i+1,"Line"][30:33]
            Suffix = sub_df.at[i+1,"Line"][47]
            Ramp_or_TR_num = sub_df.at[i+1,"Line"][44:47]
            Road_Class_top = sub_df.at[i,"Road Class"]
            if sub_df.at[i+1,"Line"][30:33]==Town_Number and sub_df.at[i+1,"Line"][33] != "9":
                if "A" in sub_df.at[i+1,"Line"][31:36] or "F" in sub_df.at[i+1,"Line"][31:36]:
                    Intersection_Route = sub_df.at[i+1,"Line"][34:38]
                else:
                    Intersection_Road = sub_df.at[i+1,"Line"][33:37]
            Tiepoint_Code = ""
            if "A" not in sub_df.at[i+1,"Line"][31:36]:
                if "SIGNAL #" in Intersection_Description:
                    Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
                else:
                    if sub_df.at[i+1,"Line"][30:33]==sub_df.at[i,"Line"][0:3] and sub_df.at[i+1,"Line"][33] == "9":
                        Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
            Bridge_Location = ""
            if sub_df.at[i,"Line"][72]=="A":
                Bridge_Location = sub_df.at[i,"Line"][73]
            Exit_Number = ""
            Exit_Suffix = ""
            if sub_df.at[i,"Line"][72]=="X":
                Exit_Number = sub_df.at[i,"Line"][73:77]
                Exit_Suffix = sub_df.at[i,"Line"][77]
            Pole_Number=""
            tiepoint_type_poles = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
            if sub_df.at[i,"Line"][72] in tiepoint_type_poles:
                Pole_Number = sub_df.at[i,"Line"][73:79]
            RR_Crossing_Number = ""
            tiepoint_type_RR = ["1","2","3","4","5","6","7","8","9"]
            if sub_df.at[i,"Line"][72] in tiepoint_type_RR:
                RR_Crossing_Number = sub_df.at[i,"Line"][73:79]
            Connector = ""
            Connector_Seq = ""
            if sub_df.at[i+1,"Line"][37]=="C":
                Connector = "C"
                Connector_Seq = sub_df.at[i+1,"Line"][38:40]
            if sub_df.at[i+1,"Line"][37] != "C":
                try:
                    if sub_df.at[i+2,"Card Number"]=="32" and sub_df.at[i+3,"Line"][37]=="C":
                        Connector = "C"
                except:
                    pass
        
            if Intersection_Description in Tiepoints_State:
                for i in range(1,100):
                    if Intersection_Description +"_"+str(i) not in Tiepoints_State:
                        Intersection_Description = Intersection_Description + "_"+str(i)
                        break
            try:
                Interchange = sub_df.at[i,"Line"][82]
            except IndexError:
                Interchange = ""
            try:
                Adt_Break=sub_df.at[i,"Line"][83]
            except IndexError:
                Adt_Break = ""
            
            Tiepoints_State[Intersection_Description] = {"Intersection Route":Intersection_Route,
                                                    "Ramp or TR #":Ramp_or_TR_num,
                                                    "Suffix":Suffix,
                                                    "Intersecting Town":Intersecting_Town,
                                                    "Intersecting Road":Intersection_Road,
                                                    "Road Class":Road_Class,
                                                    "Connector":Connector,
                                                    "Connector Seq.":Connector_Seq,
                                                    "One Way":One_Way,
                                                    "Tiepoint Code":Tiepoint_Code,
                                                    "Tiepoint Type":Tiepoint_Type,
                                                    "Bridge Prefix":Bridge_Prefix,
                                                    "Bridge Number":Bridge_Number,
                                                    "Bridge Suffix":Bridge_Suffix,
                                                    "Bridge Location":Bridge_Location,
                                                    "Exit #":Exit_Number,
                                                    "Exit Suffix":Exit_Suffix,
                                                    "Pole #":Pole_Number,
                                                    "Interchange":Interchange,
                                                    "RR Crossing #":RR_Crossing_Number,
                                                    "ADT Break":Adt_Break,
                                                    "Angle":Angle,
                                                    "HW Log Codes":Highway_Log_Codes.replace("\n","")

                                                    }
    if not section_length_count:
        for i in range(new_start+1,sub_df.shape[0]):
            if sub_df.at[i,"Card Number"]=="14" and choose_milepoint == sub_df.at[i,"Milepoint"]:
                try:
                
                    Section_Length = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
            
                except ValueError:
                    pass

    return {"Top":{"Route Name":Route_Name,
                        "Town Number":Town_Number,
                        "Road Type":Road_Type,
                        "Road Class":Road_Class_top,
                        "Signal Number":Signal_Number,
                        "Road Status":Road_Status,
                        "Latitude":Latitude,
                        "Longitude":Longitude,
                        "Reverse Latitude":Reverse_Latitude,
                        "Reverse Longitude":Reverse_Longitude},
                "Administration":{"Road Description":Road_Description,
                                  "Section Length":Section_Length,
                                  "NHS":Nhs,
                                  "Fed Aid":Fed_Aid,
                                  "R/U Designation":R_U_Designation,
                                  "Functional Class":Functional_Class,
                                  "Admin System":Admin_System,
                                  "Urban Area":Urban_Area,
                                  "Reverse Lanes":Reverse_Lanes,
                                  "Log Lanes":Log_Lanes,
                                  "Highway Type":Highway_Type,
                                  "Highway Acc. Ctrl.":Highway_Acc_Control,
                                  "On Sys Method":On_Sys_Method,
                                  "On System Year":year_formatter(On_System_Year),
                                  "ADT":Adt,
                                  "ADT Year":year_formatter(Adt_Year),
                                  "ADT Break":Adt_Break,
                                  "RL Route #":RL_Route_Number,
                                  "RL Rte. Alternative":RL_Route_Alt,
                                  "HPMS Area":Hpms_Area,
                                  "HPMS Number":Hpms_Number,
                                  "HPMS Subdivision":Hpms_Subdivision,
                                  "ADT Sample":Adt_Sample,
                                  "LIM Access Report":Limited_Access_Report,
                                  "FC Link":FC_Link,
                                  "Special System Code":Special_System_Code},
                "Pavement":{"cont or log dir":{"Section Length":Section_Length_cld,
                                                "Through Width":Through_Width_cld,
                                                "Pavement Type":Pavement_Type_cld,
                                                "Surface Thickness":Surface_Thickness_cld,
                                                "Base Thickness":Base_Thickness_cld,
                                                "Pavement Year":year_formatter(Pavement_Year_cld),
                                                "Improve Type":Improve_Type_cld,
                                                "Improve Loc":Improve_Location_cld,
                                                "State Project":State_Project_cld,
                                                "Maint Type":Maint_Type_cld,
                                                "Maint Year":year_formatter(Maint_Year_cld),
                                                "HPMS Median Type":Hpms_Median_Type_cld,
                                                "HPMS Median Width":Hpms_Median_Width_cld},
                            "cont or log wid":{"Paved Width":Paved_Width_clw,
                                                "Pavement Type":Pavement_Type_clw,
                                                "Surface Thickness":Surface_Thickness_clw,
                                                "Base Thickness":Base_Thickness_clw,
                                                "Pavement Year":year_formatter(Pavement_Year_clw),
                                                "Improve Type":Improve_Type_clw,
                                                "Improve Loc":Improve_Location_clw,
                                                "State Project":State_Project_clw},
                            "reverse direction":{"Section Length":Section_Length_rd,
                                                "Through Width":Through_Width_rd,
                                                "Pavement Type":Pavement_Type_rd,
                                                "Surface Thickness":Surface_Thickness_rd,
                                                "Base Thickness":Base_Thickness_rd,
                                                "Pavement Year":year_formatter(Pavement_Year_rd),
                                                "Improve Type":Improve_Type_rd,
                                                "Improve Loc":Improve_Location_rd,
                                                "State Project":State_Project_rd,
                                                "Maint Type":Maint_Type_rd,
                                                "Maint Year":year_formatter(Maint_Year_rd),
                                                "Town # rev. Direction":Town_Number_rd},
                            "reverse widening":{"Paved Width":Paved_Width_rw,
                                                "Pavement Type":Pavement_Type_rw,
                                                "Surface Thickness":Surface_Thickness_rw,
                                                "Base Thickness":Base_Thickness_rw,
                                                "Pavement Year":year_formatter(Pavement_Year_rw),
                                                "Improve Type":Improve_Type_rw,
                                                "Improve Loc":Improve_Location_rw,
                                                "State Project":State_Project_rw}},
                "Pavement Configuration":{"cont or log dir":{"Left Curb":Left_Curb_c,
                                                            "Left Shoulder Width":Left_Shoulder_Width_c,
                                                            "Left Shoulder Pavement":Left_Shoulder_Pavement_c,
                                                            "Left Aux Lane Type":Left_Aux_Type_c,
                                                            "Left Aux Lane Width":Left_Aux_Lane_Width_c,
                                                            "Left Aux Lane Pavement":Left_Aux_Lane_Pavement_c,
                                                            "Through Lane Width":Through_Lane_Width_c,
                                                            "Through Lane Pavement":Through_Lane_Pavement_c,
                                                            "Right Aux Lane Type":Right_Aux_Type_c,
                                                            "Right Aux Lane Width":Right_Aux_Lane_Width_c,
                                                            "Right Aux Lane Pavement":Right_Aux_Lane_Pavement_c,
                                                            "Right Shoulder Width":Right_Shoulder_Width_c,
                                                            "Right Shoulder Pavement":Right_Shoulder_Pavement_c,
                                                            "Right Curb":Right_Curb_c,
                                                            "Total Paved Width":Total_Paved_Width_c,
                                                            "Inventory Month":Inv_Month_c,
                                                            "Inventory Year":year_formatter(Inv_Year_c)},
                                            "rev dir div":{"Left Curb":Left_Curb_r,
                                                            "Left Shoulder Width":Left_Shoulder_Width_r,
                                                            "Left Shoulder Pavement":Left_Shoulder_Pavement_r,
                                                            "Left Aux Lane Type":Left_Aux_Type_r,
                                                            "Left Aux Lane Width":Left_Aux_Lane_Width_r,
                                                            "Left Aux Lane Pavement":Left_Aux_Lane_Pavement_r,
                                                            "Through Lane Width":Through_Lane_Width_r,
                                                            "Through Lane Pavement":Through_Lane_Pavement_r,
                                                            "Right Aux Lane Type":Right_Aux_Type_r,
                                                            "Right Aux Lane Width":Right_Aux_Lane_Width_r,
                                                            "Right Aux Lane Pavement":Right_Aux_Lane_Pavement_r,
                                                            "Right Shoulder Width":Right_Shoulder_Width_r,
                                                            "Right Shoulder Pavement":Right_Shoulder_Pavement_r,
                                                            "Right Curb":Right_Curb_r,
                                                            "Median Type":Median_Type_r,
                                                            "Median Width":Median_Width_r}},
                "Tiepoints":Tiepoints_State}

#################################################################################################################

def create_ramps_df(ascii_file_path):
    adict = {"Line":[],
            "Route Number":[],
            "Card Number":[],
            "Milepoint":[],
            "Road Status":[],
            "Road Class":[],
            "Town Number":[],
            "Ramp":[]}
    f = open(ascii_file_path,"r")
    for i in f:
        adict["Line"].append(i)
        adict["Route Number"].append(i[4:8].lstrip().rstrip())
        adict["Milepoint"].append(i[22:28])
        adict["Road Status"].append(i[21])
        adict["Road Class"].append(i[20])
        adict["Town Number"].append(i[0:3])
        adict["Card Number"].append(i[28:30])
        adict["Ramp"].append(i[14:18].lstrip().rstrip())

    f.close()

    df = pd.DataFrame(adict)
    #unique_routes = df["Route Number"].unique().tolist()
    df["Ramp Query"] = None
    df["Ramp Cum Miles"] = None
    count=0
    ramp_quer = ""
    ramp_cum = ""
    for row in df.itertuples():
        ramp = df.at[count,"Ramp"]
        if df.at[count,"Card Number"]=="02":
            ramp_quer = ramp + "("+df.at[count,"Line"][65:71]+")"
            ramp_cum = df.at[count,"Line"][65:72]
            if df.at[count-1,"Card Number"]=="01":
                df.at[count-1,"Ramp Query"]=ramp_quer
                df.at[count-1,"Ramp Cum Miles"] =ramp_cum
            if df.at[count-2,"Card Number"]=="00":
                df.at[count-2,"Ramp Query"]=ramp_quer
                df.at[count-2,"Ramp Cum Miles"] =ramp_cum
        df.at[count,"Ramp Query"]=ramp_quer
        df.at[count,"Ramp Cum Miles"] =ramp_cum
        count+=1

    return df

def get_unique_routes_ramps(df):
    return df["Route Number"].unique().tolist()

def get_unique_ramps_display(choose_route,df):
    return df[df["Route Number"]==choose_route]["Ramp Query"].unique().tolist()

def get_top_data_ramps(choose_route,choose_ramp_quer,df):

    choose_ramp = ""
    for i in choose_ramp_quer:
        if i == "(":
            break
        choose_ramp +=i

    get_top = df[(df["Route Number"]==choose_route) & (df["Ramp"]==choose_ramp)].reset_index()

    return {"Road Type":get_top.at[0,"Line"][3],
            "Rt. Cum Miles":get_top.at[0,"Ramp Cum Miles"][:-1],
            "Rt. Direction":get_top.at[0,"Ramp Cum Miles"][-1],
            "Road Class":get_top.at[0,"Line"][20],
            "Road Status":get_top.at[0,"Road Status"],
            "Ramp Location":get_top.at[0,"Line"][30:65].rstrip(),
            "Inventory Month":get_top.at[0,"Line"][74:76],
            "Inventory Year":year_formatter(get_top.at[0,"Line"][77:79])}

def get_unique_mp_per_route_per_ramp(choose_route,choose_ramp_quer,df):
    choose_ramp = ""
    for i in choose_ramp_quer:
        if i == "(":
            break
        choose_ramp +=i
    return df[(df["Route Number"]==choose_route) & (df["Ramp"]==choose_ramp)]["Milepoint"].unique().tolist()

def get_rest_of_data_ramps(choose_route,choose_ramp_quer,choose_milepoint,df):
    choose_ramp = ""
    for i in choose_ramp_quer:
        if i == "(":
            break
        choose_ramp +=i

    sub_df = df[(df["Route Number"]==choose_route) & (df["Ramp"]==choose_ramp)].reset_index()

    #above administration
    Town = ""
    Latitude = ""
    Longitude = ""

    for i in range(sub_df.shape[0]):
        if sub_df.at[i,"Card Number"]=="10" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Town = sub_df.at[i,"Line"][0:3]
            Latitude = sub_df.at[i,"Line"][43:52]
            Longitude = sub_df.at[i,"Line"][53:62]
            break
    if len(Town)==0:
        Town = sub_df.at[0,"Line"][0:3]


    #administration
    Ramp_Description=""
    Nhs = ""
    Fed_Aid = ""
    Urban_Area = ""
    R_U_Designation = ""
    Functional_Class = ""
    Admin_System = ""
    Reverse_Lanes = ""
    Log_Lanes=""
    Highway_Type = ""
    On_System_Year = ""
    Adt = ""
    Adt_Year=""
    #Pavement
    #Ramp Pavement
    Section_Length = 0
    section_length_count = False
    Paved_Width = ""
    Paved_Type = ""
    Pavement_Surface = ""
    Base_Thickness = ""
    Pavement_Year = ""
    Improve_Type = ""
    Imrpove_Loc = ""
    State_Project = ""
    Maint_Type = ""
    Maint_Year = ""
    #Widened Ramp Pavement
    Paved_Width_w=""
    Paved_Type_w=""
    Pavement_Surface_w=""
    Base_Thickness_w=""
    Pavement_Year_w=""
    Improve_Type_w=""
    Improve_Loc_w=""
    Improve_Loc = ""
    #Pavement Configuration
    Left_Curb = ""
    Left_Shoulder_Width = ""
    Left_Shoulder_Pavement = ""
    Left_Aux_Type = ""
    Left_Aux_Lane_Width = ""
    Left_Aux_Lane_Pavement = ""
    Through_Lane_Width = ""
    Through_Lane_Pavement = ""
    Right_Aux_Type = ""
    Right_Aux_Lane_Width = ""
    Right_Aux_Lane_Pavement = ""
    Right_Shoulder_Width = ""
    Right_Shoulder_Pavement = ""
    Right_Curb = ""
    Total_Paved_Width = ""
    Inv_Month = ""
    Inv_Year = ""
    # 001A 0 pavement type button still showing green in pavement.
    
    Tiepoints_Pavement = {}
    for i in range(sub_df.shape[0]):
        if sub_df.at[i,"Card Number"]=="02" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Ramp_Description = sub_df.at[i,"Line"][30:65]
            Section_Length = float(sub_df.at[i,"Milepoint"][:3]+'.'+sub_df.at[i,"Milepoint"][3:])
            section_length_count = True
       # if sub_df.at[i,"Card Number"]=="01" and section_length_count:
        #    Section_Length=float(sub_df.at[i,"Milepoint"][:3]+'.'+sub_df.at[i,"Milepoint"][3:])-Section_Length
         #   section_length_count=False
        if sub_df.at[i,"Card Number"]=="01" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Nhs = sub_df.at[i,"Line"][30]
            Fed_Aid = sub_df.at[i,"Line"][32]
            Urban_Area = sub_df.at[i,"Line"][38]
            R_U_Designation = sub_df.at[i,"Line"][31]
            Admin_System = sub_df.at[i,"Line"][33]
            Reverse_Lanes = sub_df.at[i,"Line"][59]
            Log_Lanes = sub_df.at[i,"Line"][60]
            Highway_Type = sub_df.at[i,"Line"][62]
            On_System_Year = sub_df.at[i,"Line"][67:71]
            Adt = sub_df.at[i,"Line"][73:79]
            Adt_Year = sub_df.at[i,"Line"][71:73]
        if sub_df.at[i,"Card Number"]=="03" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Functional_Class = sub_df.at[i,"Line"][65:67]
        if sub_df.at[i,"Card Number"]=="11" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            try:
                
                Section_Length = float(sub_df.at[i,"Line"][31:32]+"."+sub_df.at[i,"Line"][32:35])
            except ValueError:
                pass
            Paved_Width = sub_df.at[i,"Line"][38:41]
            Paved_Type = sub_df.at[i,"Line"][41:45]
            Pavement_Surface = sub_df.at[i,"Line"][45]
            Base_Thickness = sub_df.at[i,"Line"][46]
            Pavement_Year = sub_df.at[i,"Line"][47:49]
            Improve_Type = sub_df.at[i,"Line"][49]
            Improve_Loc = sub_df.at[i,"Line"][50]
            State_Project = sub_df.at[i,"Line"][54:60]
            try:
                Maint_Type = sub_df.at[i,"Line"][60]
            except IndexError:
                pass
            try:
                Maint_Year = sub_df.at[i,"Line"][61:63]
            except IndexError:
                pass
        if sub_df.at[i,"Card Number"]=="12" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Paved_Width_w = sub_df.at[i,"Line"][38:41]
            Paved_Type_w = sub_df.at[i,"Line"][41:45]
            Pavement_Surface_w = sub_df.at[i,"Line"][45]
            Base_Thickness_w = sub_df.at[i,"Line"][46]
            Pavement_Year_w = sub_df.at[i,"Line"][47:49]
            Improve_Type_w = sub_df.at[i,"Line"][49]
            Improve_Loc_w = sub_df.at[i,"Line"][50]
        if sub_df.at[i,"Card Number"]=="30" and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Left_Curb = sub_df.at[i,"Line"][30]
            Left_Shoulder_Width = sub_df.at[i,"Line"][31:33]
            Left_Shoulder_Pavement = sub_df.at[i,"Line"][33:35]
            Left_Aux_Type = sub_df.at[i,"Line"][35]
            Left_Aux_Lane_Width = sub_df.at[i,"Line"][36:38]
            Left_Aux_Lane_Pavement = sub_df.at[i,"Line"][38:40]
            Through_Lane_Width = sub_df.at[i,"Line"][40:42]
            Through_Lane_Pavement = sub_df.at[i,"Line"][42:44]
            Right_Aux_Type = sub_df.at[i,"Line"][44]
            Right_Aux_Lane_Width = sub_df.at[i,"Line"][45:47]
            Right_Aux_Lane_Pavement = sub_df.at[i,"Line"][47:49]
            Right_Shoulder_Width=sub_df.at[i,"Line"][49:51]
            Right_Shoulder_Pavement = sub_df.at[i,"Line"][51:53]
            Right_Curb = sub_df.at[i,"Line"][53]
            Total_Paved_Width = sub_df.at[i,"Line"][54:57]
            Inv_Month =sub_df.at[i,"Line"][57:59]
            Inv_Year = sub_df.at[i,"Line"][59:61]
        if int(sub_df.at[i,"Card Number"]) >= 32 and int(sub_df.at[i,"Card Number"]) <=48 and int(sub_df.at[i,"Card Number"]) %2 == 0 and choose_milepoint == sub_df.at[i,"Milepoint"]:
            Intersection_Description = sub_df.at[i,"Line"][30:65].rstrip()
            Intersection_Route = ""
            Intersection_Road = ""
            Suffix = ""
            Road_Class = ""
            Tiepoint_Type = ""
            Bridge_Prefix = ""
            Bridge_Number = ""
            Bridge_Suffix = ""
            Angle = ""
            Hw_Log_Codes = ""
            One_Way = ""
            Ramp_Or_Tr_Num = sub_df.at[i+1,"Line"][44:47]
            try:
                Suffix = sub_df.at[i+1,"Line"][47]
            except IndexError:
                pass
            Intersecting_Town = sub_df.at[i+1,"Line"][30:33]
            try:
                Road_Class = sub_df.at[i+1,"Line"][50]
            except IndexError:
                pass
            try:
                One_Way = sub_df.at[i+1,"Line"][54]
            except IndexError:
                pass
            try:
                Tiepoint_Type = sub_df.at[i,"Line"][72]
            except IndexError:
                pass
            try:
                Bridge_Prefix = sub_df.at[i,"Line"][65]
            except IndexError:
                pass
            try:
                Bridge_Number = sub_df.at[i,"Line"][66:71]
            except IndexError:
                pass
            try:
                Bridge_Suffix = sub_df.at[i,"Line"][71]
            except IndexError:
                pass
            try:
                Angle = sub_df.at[i+1,"Line"][52:54]
            except IndexError:
                pass
            try:
                Hw_Log_Codes = sub_df.at[i,"Line"][80:82].replace("\n","")
            except IndexError:
                pass
        
                #Intersection_Route = sub_df.at[i+1,"Line"][34:37]
            #if sub_df.at[i+1,"Line"][30:33]!=Town and sub_df.at[i+1,"Line"][33] != "9":
                
            if sub_df.at[i+1,"Line"][30:33]==Town and sub_df.at[i+1,"Line"][33] != "9":
                if "A" in sub_df.at[i+1,"Line"][31:36]:
                    Intersection_Route = sub_df.at[i+1,"Line"][34:38]
                else:
                    Intersection_Road = sub_df.at[i+1,"Line"][33:37]

            Tiepoint_Code = ""
            if "A" not in sub_df.at[i+1,"Line"][31:36]:
                if "SIGNAL #" in Intersection_Description:
                    Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
                else:
                    if sub_df.at[i+1,"Line"][30:33]==sub_df.at[i,"Line"][0:3] and sub_df.at[i+1,"Line"][33] == "9":
                        Tiepoint_Code = sub_df.at[i+1,"Line"][33:38]
            Bridge_Location = ""
            try:
                if sub_df.at[i,"Line"][72]=="A":
                    Bridge_Location = sub_df.at[i,"Line"][73]
            except IndexError:
                pass
            Exit_Number = ""
            Exit_Suffix = ""
            try:
                if sub_df.at[i,"Line"][72]=="X":
                    Exit_Number = sub_df.at[i,"Line"][73:77]
                    Exit_Suffix = sub_df.at[i,"Line"][77]
            except IndexError:
                pass
            Pole_Number=""
            tiepoint_type_poles = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
            try:
                if sub_df.at[i,"Line"][72] in tiepoint_type_poles:
                    Pole_Number = sub_df.at[i,"Line"][73:79]
            except IndexError:
                pass
        
            if Intersection_Description in Tiepoints_Pavement:
                for i in range(1,100):
                    if Intersection_Description +"_"+str(i) not in Tiepoints_Pavement:
                        Intersection_Description = Intersection_Description + "_"+str(i)
                        break
     
            Tiepoints_Pavement[Intersection_Description] = {"Intersection Route":Intersection_Route,
                                                    "Ramp or TR #":Ramp_Or_Tr_Num,
                                                    "Suffix":Suffix,
                                                    "Intersecting Town":Intersecting_Town,
                                                    "Intersecting Road":Intersection_Road,
                                                    "Road Class":Road_Class,
                                                    "One Way":One_Way,
                                                    "Tiepoint Code":Tiepoint_Code,
                                                    "Tiepoint Type":Tiepoint_Type,
                                                    "Bridge Prefix":Bridge_Prefix,
                                                    "Bridge Number":Bridge_Number,
                                                    "Bridge Suffix":Bridge_Suffix,
                                                    "Bridge Location":Bridge_Location,
                                                    "Exit #":Exit_Number,
                                                    "Exit Suffix":Exit_Suffix,
                                                    "Pole #":Pole_Number, 
                                                    "Angle":Angle,
                                                    "HW Log Codes":Hw_Log_Codes

                                                    }
    return {"Top":{"Town":Town,"Latitude":Latitude,"Longitude":Longitude},
            "Administration":{"Ramp Description":Ramp_Description,
                                "Nhs":Nhs,
                                "Federal Aid":Fed_Aid,
                                "Urban Area":Urban_Area,
                                "Rural Urban Designation":R_U_Designation,
                                "Functional Class":Functional_Class,
                                "Admin System":Admin_System,
                                "Reverse Lanes":Reverse_Lanes,
                                "Log Lanes":Log_Lanes,
                                "Highway Type":Highway_Type,
                                "On System Year":year_formatter(On_System_Year),
                                "Adt":Adt,
                                "Adt Year":year_formatter(Adt_Year)},
            "Pavement":{"Ramp Pavement":{"Section Length":Section_Length,
                                        "Paved Width":Paved_Width,
                                        "Pavement Type":Paved_Type,
                                        "Pavement Surface":Pavement_Surface,
                                        "Base Thickness":Base_Thickness,
                                        "Pavement Year":year_formatter(Pavement_Year),
                                        "Improve Type":Improve_Type,
                                        "Improve Loc":Improve_Loc,
                                        "State Project":State_Project,
                                        "Maint Type":Maint_Type,
                                        "Maint Year":year_formatter(Maint_Year)},
                        "Widened Ramp Pavement":{"Paved Width":Paved_Width_w,
                                                "Pavement Type":Paved_Type_w,
                                                "Pavement Surface":Pavement_Surface_w,
                                                "Base Thickness":Base_Thickness_w,
                                                "Pavement Year":year_formatter(Pavement_Year_w),
                                                "Improve Type":Improve_Type_w,
                                                "Improve Loc":Improve_Loc_w}},
            "Pavement Configuration":{"Left Curb":Left_Curb,
                                        "Left Shoulder Width":Left_Shoulder_Width,
                                        "Left Shoulder Pavement":Left_Shoulder_Pavement,
                                        "Left Aux. Lane Type":Left_Aux_Type,
                                        "Left Aux. Lane Width":Left_Aux_Lane_Width,
                                        "Left Aux. Lane Pavement":Left_Aux_Lane_Pavement,
                                        "Through Lane Width":Through_Lane_Width,
                                        "Through Lane Pavement":Through_Lane_Pavement,
                                        "Right Aux. Lane Type":Right_Aux_Type,
                                        "Right Aux. Lane Width":Right_Aux_Lane_Width,
                                        "Right Aux. Lane Pavement":Right_Aux_Lane_Pavement,
                                        "Right Shoulder Width":Right_Shoulder_Width,
                                        "Right Shoulder Pavement":Right_Shoulder_Pavement,
                                        "Right Curb":Right_Curb,
                                        "Total Paved Width":Total_Paved_Width,
                                        "Iventory Month":Inv_Month,
                                        "Inventory Year":year_formatter(Inv_Year)},
            "Tiepoints":Tiepoints_Pavement}

#fixed_size = (800,600)
#def reSize(*args):
   # Window.size = fixed_size
   # return True
#Window.bind(on_resize=reSize)

state_ascii_path = ""
town_ascii_path = ""
ramps_ascii_path = ""
sis_ascii_path = ""

def milepoint_formatter(milepoint):
    a = str(milepoint)
    if a == "0":
        return "000000"

    if "." not in a and len(a)<=3:
        
        if len(a)==1:
            a = "00"+a+"000"
            return a
        elif len(a)==2:
            a = "0"+a+"000"
            return a
        elif len(a)==3:
            a = a + "000"
            return a
    elif "." not in a and len(a)>3:
        return "000000"

    for i in range(100):
        if a.index('.') == 3:
            break
        else:
            a = "0"+a

    a = a.replace(".","")
    for i in range(100):
        if len(a) == 6:
            break
        else:
            a = a + "0"
    return a 


class WindowManager(ScreenManager):
    def __init__(self,**kwargs):
        super(WindowManager,self).__init__(**kwargs)

class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)
        self.state_button2=False
        self.town_button2=False
        self.ramp_button2=False
        self.sis_button2=False

        #lookup = Lookup(size_hint=(None,None),size=(40,40),town=True,the_input = "001")
        #self.add_widget(lookup)
        self.button_layout = FloatLayout(size=(800,600))
        self.state_button = Button(text="View State Routes",size_hint=(.25,.05),pos_hint={'x':.55,'y':.65})
        self.button_layout.add_widget(self.state_button)
        self.state_button.bind(on_press=self.state_button_clicked)

        self.browse_state_button = Button(text="Browse",size_hint=(.1,.05),pos_hint={'x':.85,'y':.65})
        self.browse_state_button.bind(on_press=self.set_state_button)
        self.browse_state_button.bind(on_press=self.file_chooser_creator)
        
        self.button_layout.add_widget(self.browse_state_button)


        self.town_button = Button(text="View Town Roads",size_hint=(.25,.05),pos_hint={'x':.55,'y':.55})
        self.button_layout.add_widget(self.town_button)
        self.town_button.bind(on_press=self.town_button_clicked)

        self.browse_town_button = Button(text="Browse",size_hint=(.1,.05),pos_hint={'x':.85,'y':.55})
        self.browse_town_button.bind(on_press=self.set_town_button)
        self.browse_town_button.bind(on_press=self.file_chooser_creator)
        
        self.button_layout.add_widget(self.browse_town_button)

        self.ramp_button = Button(text="View Ramps",size_hint=(.25,.05),pos_hint={'x':.55,'y':.45})
        self.button_layout.add_widget(self.ramp_button)
        self.ramp_button.bind(on_press=self.ramps_button_clicked)

        self.browse_ramp_button = Button(text="Browse",size_hint=(.1,.05),pos_hint={'x':.85,'y':.45})
        self.browse_ramp_button.bind(on_press=self.set_ramp_button)
        self.browse_ramp_button.bind(on_press=self.file_chooser_creator)
        
        self.button_layout.add_widget(self.browse_ramp_button)

        self.sis_button = Button(text="View State Institution Roads",size_hint=(.25,.05),pos_hint={'x':.55,'y':.35})
        self.button_layout.add_widget(self.sis_button)
        self.sis_button.bind(on_press=self.sis_button_clicked)

        self.browse_sis_button = Button(text="Browse",size_hint=(.1,.05),pos_hint={'x':.85,'y':.35})
        self.browse_sis_button.bind(on_press=self.set_sis_button)
        self.browse_sis_button.bind(on_press=self.file_chooser_creator)
        
        self.button_layout.add_widget(self.browse_sis_button)
        
        self.title_layout = FloatLayout(size=(800,600))
        self.label = Label(text="CT Department of Transportation",font_size = 35,size_hint=(.25,.05),font_name="Arial",bold=True,pos_hint={'x':.4,'y':.9},color=(0,1,0,1))
        self.label2 = Label(text=" oadway   nformation    ystem",font_size=35,size_hint=(.25,.05),font_name="Arial",pos_hint={'x':.4,'y':.8})
        self.label3 = Label(text="R",font_size=45,bold=True,size_hint=(.05,.05),font_name="Arial",pos_hint={'x':.21,'y':.8},color=(0,1,0,1))
        self.label4 = Label(text="I",font_size=45,bold=True,size_hint=(.05,.05),font_name="Arial",pos_hint={'x':.406,'y':.8},color=(0,1,0,1))
        self.label5 = Label(text="S",font_size=45,bold=True,size_hint=(.05,.05),font_name="Arial",pos_hint={'x':.649,'y':.8},color=(0,1,0,1))
        self.title_layout.add_widget(self.label)
        self.title_layout.add_widget(self.label2)
        self.title_layout.add_widget(self.label3)
        self.title_layout.add_widget(self.label4)
        self.title_layout.add_widget(self.label5)

        self.file_layout = FloatLayout(size=(800,600))

        self.state_input = TextInput(multiline=False,size_hint=(.30,.05),pos_hint={'x':.20,'y':.65})
        self.town_input = TextInput(multiline=False,size_hint=(.30,.05),pos_hint={'x':.20,'y':.55})
        self.ramp_input = TextInput(multiline=False,size_hint=(.30,.05),pos_hint={'x':.20,'y':.45})
        self.sis_input = TextInput(multiline=False,size_hint=(.30,.05),pos_hint={'x':.20,'y':.35})
        self.file_layout.add_widget(self.state_input)
        self.file_layout.add_widget(self.town_input)
        self.file_layout.add_widget(self.ramp_input)
        self.file_layout.add_widget(self.sis_input)

        self.add_widget(self.title_layout)
        self.add_widget(self.button_layout)
        self.add_widget(self.file_layout)

        self.instructions_button = Button(text="Instructions",size_hint=(.2,.05),pos_hint={'x':.38,'y':.2})
        self.instructions_button.bind(on_press=self.open_instructions)
        self.add_widget(self.instructions_button)

    def file_chooser_creator(self,*args):
        self.temp_layout = FloatLayout()
        self.temp_layout.add_widget(Button())
        self.file_chooser = FileChooserListView()
        self.file_chooser.bind(selection=self.print_selection)
        self.temp_layout.add_widget(self.file_chooser)
        remove_file_chooser_button = Button(text="Go Back",size_hint=(.1,.05),pos_hint={'x':.45,'y':0},background_color=(0,1,0,1))
        remove_file_chooser_button.bind(on_press=self.remove_file_chooser_widget)
        self.temp_layout.add_widget(remove_file_chooser_button)
        self.add_widget(self.temp_layout)

    def remove_file_chooser_widget(self,*args):
        self.state_button2=False
        self.town_button2=False
        self.ramp_button2=False
        self.sis_button2=False
        self.remove_widget(self.temp_layout)
       
    def print_selection(self,*args):
        try:
            if self.file_chooser.selection[0].split('.')[-1]=="txt":
                if self.state_button2:
                    self.state_input.text=self.file_chooser.selection[0]
                    #self.remove_widget(self.file_chooser)
                    self.remove_widget(self.temp_layout)
                    self.state_button2=False
                    self.town_button2=False
                    self.ramp_button2=False
                    self.sis_button2=False
                elif self.town_button2:
                    self.town_input.text=self.file_chooser.selection[0]
                    #self.remove_widget(self.file_chooser)
                    self.remove_widget(self.temp_layout)
                    self.state_button2=False
                    self.town_button2=False
                    self.ramp_button2=False
                    self.sis_button2=False
                elif self.ramp_button2:
                    self.ramp_input.text=self.file_chooser.selection[0]
                    #self.remove_widget(self.file_chooser)
                    self.remove_widget(self.temp_layout)
                    self.state_button2=False
                    self.town_button2=False
                    self.ramp_button2=False
                    self.sis_button2=False
                elif self.sis_button2:
                    self.sis_input.text=self.file_chooser.selection[0]
                    #self.remove_widget(self.file_chooser)
                    self.remove_widget(self.temp_layout)
                    self.state_button2=False
                    self.town_button2=False
                    self.ramp_button2=False
                    self.sis_button2=False
        except IndexError:
            pass

    def set_state_button(self,*args):
        self.state_button2=True

    def set_town_button(self,*args):
        self.town_button2=True

    def set_ramp_button(self,*args):
        self.ramp_button2=True
    
    def set_sis_button(self,*args):
        self.sis_button2 = True
        
    def open_instructions(self,*args):
        layout = FloatLayout(size=((800,600)),size_hint=(None,None))
        content = Button(text="OK",size_hint=(.1,.05),pos_hint={'x':.19,'y':0})
        layout.add_widget(content)

        inst_text = Label(text="Please upload the full path for the ASCII file in the \n text boxes below",pos_hint = {"x":-.27,"y":-.1})
        layout.add_widget(inst_text)
        inst_text_ex = Label(text="Ex."+" C:\\Users\\Desktop\\2020STATEROUTES.TXT",pos_hint = {"x":-.27,"y":-.2})
        layout.add_widget(inst_text_ex)
        popup = Popup(title = "Instructions",content=layout,auto_dismiss=False,size=(400,400),size_hint=(None,None))
        content.bind(on_press=popup.dismiss)
        popup.open()

    

    def state_button_clicked(self,btn):
        global state_ascii_path
        self.not_found=False
        try: 
            r = open(self.state_input.text,"r")
        except FileNotFoundError:
            self.not_found = True
        if not self.not_found:
            state_ascii_path = self.state_input.text
            self.manager.current = "state"
    
    def town_button_clicked(self,btn):
        global town_ascii_path
        self.not_found=False
        try:
            r = open(self.town_input.text,"r")
        except FileNotFoundError:
            self.not_found=True
        if not self.not_found:
            town_ascii_path = self.town_input.text
            self.manager.current = "town"
        
    
    def ramps_button_clicked(self,btn):
        global ramps_ascii_path
        self.not_found=False
        try:
            r=open(self.ramp_input.text,'r')
        except FileNotFoundError:
            self.not_found=True
        if not self.not_found:
            ramps_ascii_path = self.ramp_input.text
            self.manager.current = "ramps"

    def sis_button_clicked(self,btn):
        global sis_ascii_path
        self.not_found=False
        try:
            r=open(self.sis_input.text,"r")
        except FileNotFoundError:
            self.not_found=True
        if not self.not_found:
            sis_ascii_path = self.sis_input.text
            self.manager.current = "sis"

##################################################################################################################################

class StateScreen(Screen):

    def __init__(self, **kwargs):
        super(StateScreen, self).__init__(**kwargs)
      
    
    def on_enter(self):
        self.df = create_state_df(state_ascii_path)
        self.unique_routes = get_unique_routes_state(self.df)
        self.top_stuff = None
        self.route = None
        self.milepoint = None
        self.all_data = None

        


        self.cust_route_label = Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.953})
        self.add_widget(self.cust_route_label)

        self.cust_route_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.1,'y':.95},font_size = 12)
        self.add_widget(self.cust_route_input)

        self.cust_milepoint_label = Label(text="Milepoint:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.2,'y':.953})
        self.add_widget(self.cust_milepoint_label)

        self.cust_milepoint_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.3,'y':.95},font_size = 12)
        self.add_widget(self.cust_milepoint_input)

        self.search_button = Button(text="Search",size_hint=(.14,.04),pos_hint={'x':.4,'y':.95})
        
        self.search_button.bind(on_press=self.create_options)
        self.search_button.bind(on_press=self.search_clicked_set_milepoint)
        self.search_button.bind(on_press=self.create_milepoints)
        self.search_button.bind(on_press=self.insert_log_direction)
        self.search_button.bind(on_press=self.insert_inv_month)
        self.search_button.bind(on_press=self.insert_inv_year)
        self.search_button.bind(on_press=self.search_clicked_set_route)
        
        self.search_button.bind(on_press=self.search_get_top_stuff)
       
        self.add_widget(self.search_button)

        self.first_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.82})
        self.add_widget(self.first_page_line)

        
        self.route_dropdown = DropDown()
        for route in self.unique_routes:
            self.route_button = Button(text=route,size_hint_y = None, height = 20)
            self.route_button.bind(on_release=lambda route_button: self.route_dropdown.select(route_button.text))
            self.route_dropdown.add_widget(self.route_button)

        self.main_route_button = Button(text="Choose Route",size_hint=(.14,.04),pos_hint={'x':.1,'y':.9})
        self.main_route_button.bind(on_release=self.route_dropdown.open)

        self.route_dropdown.bind(on_select=self.create_milepoints)
        self.route_dropdown.bind(on_select=self.insert_log_direction)
        self.route_dropdown.bind(on_select=self.insert_inv_month)
        self.route_dropdown.bind(on_select=self.insert_inv_year)
        self.route_dropdown.bind(on_select=self.set_route)
        self.route_dropdown.bind(on_select=self.get_top_stuff)
        
        self.route_dropdown.bind(on_select=lambda instance, x: setattr(self.main_route_button,'text',x))
        
        self.add_widget(self.main_route_button)
        #route label
        self.route_label=Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.903})
        self.add_widget(self.route_label)

        self.log_direction_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.41,'y':.9},font_size = 12)
        self.add_widget(self.log_direction_input)

        self.log_direction_label=Label(text="Log Direction:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.3,'y':.903})
        self.add_widget(self.log_direction_label)

        self.inv_month_year_label=Label(text="Inventory Mo./Yr.:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.55,'y':.903})
        self.add_widget(self.inv_month_year_label)

        self.inv_month_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.7,'y':.9},font_size = 12)
        self.add_widget(self.inv_month_input)

        self.inv_year_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.8,'y':.9},font_size = 12)
        self.add_widget(self.inv_year_input)

        self.btn2 = Button(text="Go Home",size_hint=(.1,.05),pos_hint={'x':.45,'y':.03})
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.prev_page)
        
    def create_milepoints(self,*args):
        if self.route is not None:

            try:
                self.remove_widget(self.main_milepoint_button)
                self.remove_widget(self.milepoint_button)
                self.remove_widget(self.milepoint_label)
                self.milepoints_formatter()
                
            except AttributeError:
                self.milepoints_formatter()
                

    def milepoints_formatter(self,*args):
        unique_milepoints = get_unique_milepoints_per_route_state(self.route,self.df)
        self.unique_milepoints = unique_milepoints
        
        self.milepoint_dropdown=DropDown()
        for milepoint in self.unique_milepoints:
            self.milepoint_button = Button(text=str(float(milepoint[:3]+'.'+milepoint[3:])),size_hint_y = None, height = 20)
            self.milepoint_button.bind(on_release=lambda milepoint_button: self.milepoint_dropdown.select(milepoint_button.text))
            self.milepoint_dropdown.add_widget(self.milepoint_button)
        self.main_milepoint_button = Button(text="Choose Milepoint",size_hint=(.20,.04),pos_hint={'x':.43,'y':.82})
        self.main_milepoint_button.bind(on_release=self.milepoint_dropdown.open)

        self.milepoint_dropdown.bind(on_select=self.create_options)
        self.milepoint_dropdown.bind(on_select=self.set_milepoint)
        self.milepoint_dropdown.bind(on_select=lambda instance, x: setattr(self.main_milepoint_button,'text',x))
                

        self.add_widget(self.main_milepoint_button)
        self.milepoint_label=Label(text="Milepoint:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.317,'y':.823})
        self.add_widget(self.milepoint_label)        
        
    def create_options(self,*args):
        if self.milepoint is not None:
            
            try:
                # remove buttons
                #all_data = state_getter_functions.get_rest_of_data(self.route,milepoint_formatter(self.milepoint),self.df)
                self.remove_widget(self.administration_button)
                self.remove_widget(self.pavement_button)
                self.remove_widget(self.pavconfig_button)
                self.remove_widget(self.tiepoints_button)
                # remove top stuff
                self.remove_widget(self.route_name_input)
                self.remove_widget(self.route_name_label)
                self.remove_widget(self.town_number_input)
                self.remove_widget(self.town_number_label)
                self.remove_widget(self.road_class_input)
                self.remove_widget(self.road_class_label)
                self.remove_widget(self.road_type_input)
                self.remove_widget(self.road_type_label)
                self.remove_widget(self.road_status_input)
                self.remove_widget(self.road_status_label)
                self.remove_widget(self.signal_number_input)
                self.remove_widget(self.signal_number_label)
                self.remove_widget(self.latitude_input)
                self.remove_widget(self.latitude_label)
                self.remove_widget(self.longitude_input)
                self.remove_widget(self.longitude_label)
                self.remove_widget(self.reverse_latitude_input)
                self.remove_widget(self.reverse_latitude_label)
                self.remove_widget(self.reverse_longitude_input)
                self.remove_widget(self.reverse_longitude_label)
                self.remove_widget(self.second_page_line)

                self.remove_widget(self.scroll)

                self.options_formatter()


            except AttributeError:
                self.options_formatter()
                

    def options_formatter(self,*args):
        self.second_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.45})
        self.add_widget(self.second_page_line)
        #buttons
        self.all_data = get_rest_of_data_state(self.route,milepoint_formatter(self.milepoint),self.df)

        self.administration_button = Button(text="View Administration",size_hint=(.20,.04),pos_hint={'x':.02,'y':.4})
        self.administration_button.bind(on_press=self.administration_button_clicked)
        self.add_widget(self.administration_button)

        self.pavement_button = Button(text="View Pavement",size_hint=(.20,.04),pos_hint={'x':.02,'y':.3})
        self.pavement_button.bind(on_press=self.pavement_button_clicked)
        self.add_widget(self.pavement_button)

        self.pavconfig_button = Button(text="View Pavement Config.",size_hint=(.20,.04),pos_hint={'x':.02,'y':.2})
        self.pavconfig_button.bind(on_press=self.pavement_config_button_clicked)
        self.add_widget(self.pavconfig_button)

        self.tiepoints_button = Button(text="View Tiepoints",size_hint=(.20,.04),pos_hint={'x':.02,'y':.1})
        self.tiepoints_button.bind(on_press=self.tiepoints_button_clicked)
        self.add_widget(self.tiepoints_button)
        #top stuff
        self.route_name_input = TextInput(multiline=False,size_hint=(.3,.04),pos_hint={'x':.17,'y':.75},font_size = 12)
        self.route_name_input.text = self.all_data["Top"]["Route Name"]
        self.add_widget(self.route_name_input)

        self.route_name_label=Label(text="Route Name:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.753})
        self.add_widget(self.route_name_label)

        self.signal_number_input = TextInput(multiline=False,size_hint=(.2,.04),pos_hint={'x':.67,'y':.75},font_size = 12)
        self.signal_number_input.text = self.all_data["Top"]["Signal Number"]
        self.add_widget(self.signal_number_input)

        self.signal_number_label=Label(text="Signal Number:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.55,'y':.753})
        self.add_widget(self.signal_number_label)

        self.town_number_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.04,'y':.65},font_size = 12)
        self.town_number_input.text = self.all_data["Top"]["Town Number"]
        self.add_widget(self.town_number_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.1,'y':.65},the_input =self.town_number_input.text)
        self.add_widget(lookup)

        self.town_number_label=Label(text="Town #:",font_size = 16,size_hint=(.04,.04),font_name="Arial",pos_hint={'x':.05,'y':.7033})
        self.add_widget(self.town_number_label)

        self.road_class_label=Label(text="Road Class:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.05,'y':.6033})
        self.add_widget(self.road_class_label)

        self.road_class_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.04,'y':.55},font_size = 12)
        self.road_class_input.text = self.all_data["Top"]["Road Class"]
        self.add_widget(self.road_class_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.1,'y':.55},the_input =self.road_class_input.text)
        self.add_widget(lookup)

        self.road_type_label=Label(text="Road Type:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.2,'y':.7033})
        self.add_widget(self.road_type_label)

        self.road_type_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.2,'y':.65},font_size = 12)
        self.road_type_input.text = self.all_data["Top"]["Road Type"]
        self.add_widget(self.road_type_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_type=True,pos_hint={"x":.26,'y':.65},the_input =self.road_type_input.text)
        self.add_widget(lookup)

        self.road_status_label=Label(text="Road Status:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.2,'y':.6033})
        self.add_widget(self.road_status_label)

        self.road_status_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.2,'y':.55},font_size = 12)
        self.road_status_input.text = self.all_data["Top"]["Road Status"]
        self.add_widget(self.road_status_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_status=True,pos_hint={"x":.26,'y':.55},the_input =self.road_status_input.text)
        self.add_widget(lookup)

        self.latitude_label=Label(text="Latitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.5,'y':.7033})
        self.add_widget(self.latitude_label)

        self.latitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.49,'y':.65},font_size = 12)
        self.latitude_input.text = self.all_data["Top"]["Latitude"][0:2]+" " + self.all_data["Top"]["Latitude"][2:4] + " " + self.all_data["Top"]["Latitude"][4:]
        self.add_widget(self.latitude_input)

        self.longitude_label=Label(text="Longitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.7,'y':.7033})
        self.add_widget(self.longitude_label)

        self.longitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.69,'y':.65},font_size = 12)
        self.longitude_input.text = self.all_data["Top"]["Longitude"][0:2]+" " + self.all_data["Top"]["Longitude"][2:4] + " " + self.all_data["Top"]["Longitude"][4:]
        self.add_widget(self.longitude_input)

        self.reverse_latitude_label=Label(text=" Reverse Latitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.5,'y':.6033})
        self.add_widget(self.reverse_latitude_label)

        self.reverse_latitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.49,'y':.55},font_size = 12)
        self.reverse_latitude_input.text = self.all_data["Top"]["Reverse Latitude"][0:2]+" " + self.all_data["Top"]["Reverse Latitude"][2:4] + " " + self.all_data["Top"]["Reverse Latitude"][4:]
        self.add_widget(self.reverse_latitude_input)

        self.reverse_longitude_label=Label(text="Reverse Longitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.7,'y':.6033})
        self.add_widget(self.reverse_longitude_label)

        self.reverse_longitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.69,'y':.55},font_size = 12)
        self.reverse_longitude_input.text = self.all_data["Top"]["Reverse Longitude"][0:2]+" " + self.all_data["Top"]["Reverse Longitude"][2:4] + " " + self.all_data["Top"]["Reverse Longitude"][4:]
        self.add_widget(self.reverse_longitude_input)

    def administration_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Administration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Administration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=2,size_hint=(1,1))
        label = Label(text="Road Description:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        embed.add_widget(TextInput(text = data["Road Description"],multiline=False,font_size = 12,size_hint_x=None,width=250))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="NHS:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Fed Aid:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = str(data["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["NHS"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Fed Aid"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),fed_aid=True,pos_hint={"x":.75,'y':0},the_input = data["Fed Aid"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="R/U Designation:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Funct. Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Admin System:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["R/U Designation"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),r_u_designation=True,pos_hint={"x":.084,'y':0},the_input = data["R/U Designation"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Functional Class"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),functional_class=True,pos_hint={"x":.417,'y':0},the_input = data["Functional Class"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Admin System"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),admin_system=True,pos_hint={"x":.75,'y':0},the_input = data["Admin System"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Urban Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Reverse Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Log Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Urban Area"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),urban_area=True,pos_hint={"x":.084,'y':0},the_input = data["Urban Area"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Reverse Lanes"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Log Lanes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Highway Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Highway Acc. Ctrl:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="On Sys. Method:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Highway Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),highway_type=True,pos_hint={"x":.084,'y':0},the_input = data["Highway Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Highway Acc. Ctrl."],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),highway_acc=True,pos_hint={"x":.417,'y':0},the_input = data["Highway Acc. Ctrl."])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["On Sys Method"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),on_sys_method=True,pos_hint={"x":.75,'y':0},the_input = data["On Sys Method"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="On System Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["On System Year"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["ADT"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=100))
        embed.add_widget(TextInput(text = data["ADT Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="ADT Break:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="RL Route #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="RL Rte Alternative:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["ADT Break"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["RL Route #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=100))
        embed.add_widget(TextInput(text = data["RL Rte. Alternative"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),rl_alt=True,pos_hint={"x":.75,'y':0},the_input = data["RL Rte. Alternative"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="HPMS Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Subdivision:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["HPMS Area"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["HPMS Number"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["HPMS Subdivision"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="ADT Sample:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="LIM Access Report:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="FC Link:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["ADT Sample"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["LIM Access Report"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),lim_access=True,pos_hint={"x":.417,'y':0},the_input = data["LIM Access Report"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["FC Link"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Special System Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Special System Code"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),special_system_code=True,pos_hint={"x":.084,'y':0},the_input = data["Special System Code"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

       
        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        
      
        self.add_widget(self.scroll)
        


    def pavement_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Direction",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Through Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =str(data['cont or log dir']["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Through Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data['cont or log dir']["Pavement Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.76,'y':0},the_input = data['cont or log dir']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log dir']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log dir']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Maint. Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Maint. Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Maint Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),maint_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Maint Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Maint Year"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="HPMS Median Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Median Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["HPMS Median Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),hpms_median_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["HPMS Median Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["HPMS Median Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Widening",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text = data['cont or log wid']["Pavement Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.5,'y':0},the_input = data['cont or log wid']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log wid']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log wid']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log wid']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log wid']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log wid']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log wid']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log wid']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log wid']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Direction",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Through Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =str(data['reverse direction']["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        embed.add_widget(TextInput(text =  data['reverse direction']["Through Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data['reverse direction']["Pavement Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.76,'y':0},the_input = data['reverse direction']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['reverse direction']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse direction']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['reverse direction']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse direction']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Maint. Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Maint. Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Town # Reverse Dir:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Maint Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),maint_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Maint Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Maint Year"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text =  data['reverse direction']["Town # rev. Direction"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.833,'y':0},the_input = data['reverse direction']["Town # rev. Direction"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Widening",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text = data['reverse widening']["Pavement Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.5,'y':0},the_input = data['reverse widening']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['reverse widening']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse widening']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['reverse widening']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse widening']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse widening']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse widening']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['reverse widening']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse widening']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def pavement_config_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement Configuration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement Configuration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Direction of Divided Highway",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Left Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Aux Lane Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Left Aux Lane Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Aux Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Aux Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Left Aux Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Thru Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Thru Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Through Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Through Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Through Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Aux Lane Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Aux Lane Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Aux Lane Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Aux Lane Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Aux Lane Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Curb"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Right Curb"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Total Paved Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Inventory Month-Year:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Total Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data['cont or log dir']["Inventory Month"]+"-"+data['cont or log dir']['Inventory Year'],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Direction of a Divided Highway",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Left Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Aux Lane Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Left Aux Lane Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Aux Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Aux Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Left Aux Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Thru Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Thru Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Through Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['rev dir div']["Through Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Through Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Aux Lane Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Aux Lane Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Aux Lane Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Aux Lane Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Aux Lane Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Curb"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Right Curb"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Median Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Median Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Median Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),hpms_median_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Median Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Median Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)



        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def tiepoints_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Tiepoints"]
#go back here
        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Tiepoints",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        num_tiepoints = 1
        for k,v in data.items():
            embed = GridLayout(cols=1,size_hint=(1,1))
            label = Label(text="Tiepoint"+" "+str(num_tiepoints),font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            new_desc = ""
            if k[:-2] in data:
                new_desc=k[:-2]
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = new_desc,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)
            else:
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = k,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Route:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Ramp or TR #",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersection Route"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=75))
            embed.add_widget(TextInput(text = data[k]["Ramp or TR #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
            #lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
            #embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Town:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Intersecting Road",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Road Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersecting Town"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.084,'y':0},the_input = data[k]["Intersecting Town"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Intersecting Road"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Road Class"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Road Class"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Connector:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Connector Seq.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="One Way:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Connector"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Connector Seq."],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["One Way"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),one_way=True,pos_hint={"x":.75,'y':0},the_input =data[k]["One Way"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Tiepoint Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Tiepoint Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Prefix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Tiepoint Code"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_code=True,pos_hint={"x":.084,'y':0},the_input = data[k]["Tiepoint Code"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Tiepoint Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_type=True,pos_hint={"x":.417,'y':0},the_input =data[k]["Tiepoint Type"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Bridge Prefix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_prefix=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Bridge Prefix"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Bridge Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Location:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Bridge Number"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
            embed.add_widget(TextInput(text = data[k]["Bridge Suffix"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Bridge Location"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_location=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Bridge Location"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Exit #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Exit Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Pole Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Exit #"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["Exit Suffix"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["Pole #"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Interchange:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="ATR #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="RR Crossing #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Interchange"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = "",pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["RR Crossing #"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="ADT Break:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Angle:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="HW Log Codes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["ADT Break"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text =data[k]["Angle"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["HW Log Codes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),hw_log_code=True,pos_hint={"x":.75,'y':0},the_input =data[k]["HW Log Codes"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)
            
# go back here


            num_tiepoints+=1


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

        
        

    def get_all_stuff(self,*args):
        self.all_data = get_rest_of_data_state(self.route,milepoint_formatter(self.milepoint),self.df)
    
    def get_top_stuff(self,*args):
        self.top_stuff = get_top_data_state(self.main_route_button.text,self.df)

    def search_get_top_stuff(self,*args):
        self.top_stuff = get_top_data_state(self.cust_route_input.text,self.df)

    def set_milepoint(self,*args):
        self.milepoint = self.main_milepoint_button.text

    def set_route(self,*args):
        self.route = self.main_route_button.text

    def search_clicked_set_route(self,*args):
        self.main_route_button.text = self.cust_route_input.text
        self.route = self.cust_route_input.text

    def search_clicked_set_milepoint(self,*args):
        self.main_milepoint_button.text = self.cust_milepoint_input.text
        self.milepoint = self.cust_milepoint_input.text

    def insert_log_direction(self,*args):
        if self.top_stuff is not None:
            self.log_direction_input.text = self.top_stuff['Log Direction']

    def insert_inv_month(self,*args):
        if self.top_stuff is not None:
            self.inv_month_input.text = self.top_stuff['Inventory Month']

    def insert_inv_year(self,*args):
        if self.top_stuff is not None:
            self.inv_year_input.text = self.top_stuff['Inventory Year']
    
    def prev_page(self,instance):
        self.clear_widgets()
        self.manager.current = "title"

####################################################################################################################################

class SisScreen(Screen):
    def __init__(self, **kwargs):
        super(SisScreen, self).__init__(**kwargs)
        

    def on_enter(self):
        self.df = create_sis_df(sis_ascii_path)
        self.unique_routes = get_unique_routes_sis(self.df)
        self.top_stuff = None
        self.route = None
        self.milepoint = None
        self.all_data = None

        


        self.cust_route_label = Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.953})
        self.add_widget(self.cust_route_label)

        self.cust_route_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.1,'y':.95},font_size = 12)
        self.add_widget(self.cust_route_input)

        self.cust_milepoint_label = Label(text="Milepoint:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.2,'y':.953})
        self.add_widget(self.cust_milepoint_label)

        self.cust_milepoint_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.3,'y':.95},font_size = 12)
        self.add_widget(self.cust_milepoint_input)

        self.search_button = Button(text="Search",size_hint=(.14,.04),pos_hint={'x':.4,'y':.95})
        
        self.search_button.bind(on_press=self.create_options)
        self.search_button.bind(on_press=self.search_clicked_set_milepoint)
        self.search_button.bind(on_press=self.create_milepoints)
        self.search_button.bind(on_press=self.insert_log_direction)
        self.search_button.bind(on_press=self.insert_inv_month)
        self.search_button.bind(on_press=self.insert_inv_year)
        self.search_button.bind(on_press=self.search_clicked_set_route)
        
        self.search_button.bind(on_press=self.search_get_top_stuff)
       
        self.add_widget(self.search_button)

        self.first_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.82})
        self.add_widget(self.first_page_line)

        
        self.route_dropdown = DropDown()
        for route in self.unique_routes:
            self.route_button = Button(text=route,size_hint_y = None, height = 20)
            self.route_button.bind(on_release=lambda route_button: self.route_dropdown.select(route_button.text))
            self.route_dropdown.add_widget(self.route_button)

        self.main_route_button = Button(text="Choose Route",size_hint=(.14,.04),pos_hint={'x':.1,'y':.9})
        self.main_route_button.bind(on_release=self.route_dropdown.open)

        self.route_dropdown.bind(on_select=self.create_milepoints)
        self.route_dropdown.bind(on_select=self.insert_log_direction)
        self.route_dropdown.bind(on_select=self.insert_inv_month)
        self.route_dropdown.bind(on_select=self.insert_inv_year)
        self.route_dropdown.bind(on_select=self.set_route)
        self.route_dropdown.bind(on_select=self.get_top_stuff)
        
        self.route_dropdown.bind(on_select=lambda instance, x: setattr(self.main_route_button,'text',x))
        
        self.add_widget(self.main_route_button)
        #route label
        self.route_label=Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.903})
        self.add_widget(self.route_label)

        self.log_direction_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.41,'y':.9},font_size = 12)
        self.add_widget(self.log_direction_input)

        self.log_direction_label=Label(text="Log Direction:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.3,'y':.903})
        self.add_widget(self.log_direction_label)

        self.inv_month_year_label=Label(text="Inventory Mo./Yr.:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.55,'y':.903})
        self.add_widget(self.inv_month_year_label)

        self.inv_month_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.7,'y':.9},font_size = 12)
        self.add_widget(self.inv_month_input)

        self.inv_year_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.8,'y':.9},font_size = 12)
        self.add_widget(self.inv_year_input)

        self.btn2 = Button(text="Go Home",size_hint=(.1,.05),pos_hint={'x':.45,'y':.03})
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.prev_page)
        
    def create_milepoints(self,*args):
        if self.route is not None:

            try:
                self.remove_widget(self.main_milepoint_button)
                self.remove_widget(self.milepoint_button)
                self.remove_widget(self.milepoint_label)
                self.milepoints_formatter()
                
            except AttributeError:
                self.milepoints_formatter()
                

    def milepoints_formatter(self,*args):
        unique_milepoints = get_unique_milepoints_per_route_sis(self.route,self.df)
        self.unique_milepoints = unique_milepoints
        
        self.milepoint_dropdown=DropDown()
        for milepoint in self.unique_milepoints:
            self.milepoint_button = Button(text=str(float(milepoint[:3]+'.'+milepoint[3:])),size_hint_y = None, height = 20)
            self.milepoint_button.bind(on_release=lambda milepoint_button: self.milepoint_dropdown.select(milepoint_button.text))
            self.milepoint_dropdown.add_widget(self.milepoint_button)
        self.main_milepoint_button = Button(text="Choose Milepoint",size_hint=(.20,.04),pos_hint={'x':.43,'y':.82})
        self.main_milepoint_button.bind(on_release=self.milepoint_dropdown.open)

        self.milepoint_dropdown.bind(on_select=self.create_options)
        self.milepoint_dropdown.bind(on_select=self.set_milepoint)
        self.milepoint_dropdown.bind(on_select=lambda instance, x: setattr(self.main_milepoint_button,'text',x))
                

        self.add_widget(self.main_milepoint_button)
        self.milepoint_label=Label(text="Milepoint:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.317,'y':.823})
        self.add_widget(self.milepoint_label)        
        
    def create_options(self,*args):
        if self.milepoint is not None:
            
            try:
                # remove buttons
                #all_data = state_getter_functions.get_rest_of_data(self.route,milepoint_formatter(self.milepoint),self.df)
                self.remove_widget(self.administration_button)
                self.remove_widget(self.pavement_button)
                self.remove_widget(self.pavconfig_button)
                self.remove_widget(self.tiepoints_button)
                # remove top stuff
                self.remove_widget(self.route_name_input)
                self.remove_widget(self.route_name_label)
                self.remove_widget(self.town_number_input)
                self.remove_widget(self.town_number_label)
                self.remove_widget(self.road_class_input)
                self.remove_widget(self.road_class_label)
                self.remove_widget(self.road_type_input)
                self.remove_widget(self.road_type_label)
                self.remove_widget(self.road_status_input)
                self.remove_widget(self.road_status_label)
                self.remove_widget(self.signal_number_input)
                self.remove_widget(self.signal_number_label)
                self.remove_widget(self.latitude_input)
                self.remove_widget(self.latitude_label)
                self.remove_widget(self.longitude_input)
                self.remove_widget(self.longitude_label)
                self.remove_widget(self.reverse_latitude_input)
                self.remove_widget(self.reverse_latitude_label)
                self.remove_widget(self.reverse_longitude_input)
                self.remove_widget(self.reverse_longitude_label)
                self.remove_widget(self.second_page_line)

                self.remove_widget(self.scroll)

                self.options_formatter()


            except AttributeError:
                self.options_formatter()
                

    def options_formatter(self,*args):
        self.second_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.45})
        self.add_widget(self.second_page_line)
        #buttons
        self.all_data = get_rest_of_data_sis(self.route,milepoint_formatter(self.milepoint),self.df)

        self.administration_button = Button(text="View Administration",size_hint=(.20,.04),pos_hint={'x':.02,'y':.4})
        self.administration_button.bind(on_press=self.administration_button_clicked)
        self.add_widget(self.administration_button)

        self.pavement_button = Button(text="View Pavement",size_hint=(.20,.04),pos_hint={'x':.02,'y':.3})
        self.pavement_button.bind(on_press=self.pavement_button_clicked)
        self.add_widget(self.pavement_button)

        self.pavconfig_button = Button(text="View Pavement Config.",size_hint=(.20,.04),pos_hint={'x':.02,'y':.2})
        self.pavconfig_button.bind(on_press=self.pavement_config_button_clicked)
        self.add_widget(self.pavconfig_button)

        self.tiepoints_button = Button(text="View Tiepoints",size_hint=(.20,.04),pos_hint={'x':.02,'y':.1})
        self.tiepoints_button.bind(on_press=self.tiepoints_button_clicked)
        self.add_widget(self.tiepoints_button)
        #top stuff
        self.route_name_input = TextInput(multiline=False,size_hint=(.3,.04),pos_hint={'x':.17,'y':.75},font_size = 12)
        self.route_name_input.text = self.all_data["Top"]["Route Name"]
        self.add_widget(self.route_name_input)

        self.route_name_label=Label(text="Route Name:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.753})
        self.add_widget(self.route_name_label)

        self.signal_number_input = TextInput(multiline=False,size_hint=(.2,.04),pos_hint={'x':.67,'y':.75},font_size = 12)
        self.signal_number_input.text = self.all_data["Top"]["Signal Number"]
        self.add_widget(self.signal_number_input)

        self.signal_number_label=Label(text="Signal Number:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.55,'y':.753})
        self.add_widget(self.signal_number_label)

        self.town_number_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.04,'y':.65},font_size = 12)
        self.town_number_input.text = self.all_data["Top"]["Town Number"]
        self.add_widget(self.town_number_input)

        self.town_number_label=Label(text="Town #:",font_size = 16,size_hint=(.04,.04),font_name="Arial",pos_hint={'x':.05,'y':.7033})
        self.add_widget(self.town_number_label)

        lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.1,'y':.65},the_input =self.town_number_input.text)
        self.add_widget(lookup)

        self.road_class_label=Label(text="Road Class:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.05,'y':.6033})
        self.add_widget(self.road_class_label)

        self.road_class_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.04,'y':.55},font_size = 12)
        self.road_class_input.text = self.all_data["Top"]["Road Class"]
        self.add_widget(self.road_class_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.1,'y':.55},the_input =self.road_class_input.text)
        self.add_widget(lookup)

        self.road_type_label=Label(text="Road Type:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.2,'y':.7033})
        self.add_widget(self.road_type_label)

        self.road_type_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.2,'y':.65},font_size = 12)
        self.road_type_input.text = self.all_data["Top"]["Road Type"]
        self.add_widget(self.road_type_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_type=True,pos_hint={"x":.26,'y':.65},the_input =self.road_type_input.text)
        self.add_widget(lookup)

        self.road_status_label=Label(text="Road Status:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.2,'y':.6033})
        self.add_widget(self.road_status_label)

        self.road_status_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.2,'y':.55},font_size = 12)
        self.road_status_input.text = self.all_data["Top"]["Road Status"]
        self.add_widget(self.road_status_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_status=True,pos_hint={"x":.26,'y':.55},the_input =self.road_status_input.text)
        self.add_widget(lookup)

        self.latitude_label=Label(text="Latitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.5,'y':.7033})
        self.add_widget(self.latitude_label)

        self.latitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.49,'y':.65},font_size = 12)
        self.latitude_input.text = self.all_data["Top"]["Latitude"][0:2]+" " + self.all_data["Top"]["Latitude"][2:4] + " " + self.all_data["Top"]["Latitude"][4:]
        self.add_widget(self.latitude_input)

        self.longitude_label=Label(text="Longitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.7,'y':.7033})
        self.add_widget(self.longitude_label)

        self.longitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.69,'y':.65},font_size = 12)
        self.longitude_input.text = self.all_data["Top"]["Longitude"][0:2]+" " + self.all_data["Top"]["Longitude"][2:4] + " " + self.all_data["Top"]["Longitude"][4:]
        self.add_widget(self.longitude_input)

        self.reverse_latitude_label=Label(text=" Reverse Latitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.5,'y':.6033})
        self.add_widget(self.reverse_latitude_label)

        self.reverse_latitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.49,'y':.55},font_size = 12)
        self.reverse_latitude_input.text = self.all_data["Top"]["Reverse Latitude"][0:2]+" " + self.all_data["Top"]["Reverse Latitude"][2:4] + " " + self.all_data["Top"]["Reverse Latitude"][4:]
        self.add_widget(self.reverse_latitude_input)

        self.reverse_longitude_label=Label(text="Reverse Longitude:",font_size = 16,size_hint=(.07,.04),font_name="Arial",pos_hint={'x':.7,'y':.6033})
        self.add_widget(self.reverse_longitude_label)

        self.reverse_longitude_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.69,'y':.55},font_size = 12)
        self.reverse_longitude_input.text = self.all_data["Top"]["Reverse Longitude"][0:2]+" " + self.all_data["Top"]["Reverse Longitude"][2:4] + " " + self.all_data["Top"]["Reverse Longitude"][4:]
        self.add_widget(self.reverse_longitude_input)

    def administration_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Administration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Administration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=2,size_hint=(1,1))
        label = Label(text="Road Description:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        embed.add_widget(TextInput(text = data["Road Description"],multiline=False,font_size = 12,size_hint_x=None,width=250))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="NHS:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Fed Aid:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = str(data["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["NHS"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Fed Aid"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),fed_aid=True,pos_hint={"x":.75,'y':0},the_input = data["Fed Aid"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="R/U Designation:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Funct. Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Admin System:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["R/U Designation"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),r_u_designation=True,pos_hint={"x":.084,'y':0},the_input =  data["R/U Designation"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Functional Class"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),functional_class=True,pos_hint={"x":.417,'y':0},the_input = data["Functional Class"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Admin System"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),admin_system=True,pos_hint={"x":.75,'y':0},the_input = data["Admin System"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Urban Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Reverse Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Log Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Urban Area"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),urban_area=True,pos_hint={"x":.084,'y':0},the_input = data["Urban Area"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Reverse Lanes"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Log Lanes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Highway Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Highway Acc. Ctrl:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="On Sys. Method:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Highway Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),highway_type=True,pos_hint={"x":.084,'y':0},the_input = data["Highway Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Highway Acc. Ctrl."],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),highway_acc=True,pos_hint={"x":.417,'y':0},the_input = data["Highway Acc. Ctrl."])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["On Sys Method"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),on_sys_method=True,pos_hint={"x":.75,'y':0},the_input = data["On Sys Method"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="On System Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["On System Year"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["ADT"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=100))
        embed.add_widget(TextInput(text = data["ADT Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="ADT Break:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="RL Route #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="RL Rte Alternative:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["ADT Break"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["RL Route #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=100))
        embed.add_widget(TextInput(text = data["RL Rte. Alternative"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),rl_alt=True,pos_hint={"x":.75,'y':0},the_input = data["RL Rte. Alternative"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="HPMS Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Subdivision:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["HPMS Area"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["HPMS Number"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text = data["HPMS Subdivision"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="ADT Sample:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="LIM Access Report:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="FC Link:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["ADT Sample"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["LIM Access Report"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),lim_access=True,pos_hint={"x":.417,'y':0},the_input = data["LIM Access Report"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["FC Link"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Special System Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Special System Code"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),special_system_code=True,pos_hint={"x":.084,'y':0},the_input = data["Special System Code"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

       
        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        
      
        self.add_widget(self.scroll)


    def pavement_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Direction",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Through Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =str(data['cont or log dir']["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Through Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data['cont or log dir']["Pavement Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.76,'y':0},the_input = data['cont or log dir']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log dir']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log dir']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Maint. Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Maint. Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Maint Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),maint_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Maint Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["Maint Year"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="HPMS Median Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Median Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["HPMS Median Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),hpms_median_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["HPMS Median Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log dir']["HPMS Median Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Widening",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text = data['cont or log wid']["Pavement Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.5,'y':0},the_input = data['cont or log wid']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log wid']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log wid']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log wid']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log wid']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log wid']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log wid']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['cont or log wid']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['cont or log wid']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log wid']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Direction",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Through Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =str(data['reverse direction']["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        embed.add_widget(TextInput(text =  data['reverse direction']["Through Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data['reverse direction']["Pavement Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.76,'y':0},the_input = data['reverse direction']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['reverse direction']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse direction']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['reverse direction']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse direction']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Maint. Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Maint. Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Town # Reverse Dir:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse direction']["Maint Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),maint_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse direction']["Maint Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse direction']["Maint Year"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text =  data['reverse direction']["Town # rev. Direction"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.833,'y':0},the_input = data['reverse direction']["Town # rev. Direction"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Widening",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        embed.add_widget(TextInput(text = data['reverse widening']["Pavement Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.5,'y':0},the_input = data['reverse widening']["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Surface Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Surface Thickness"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data['reverse widening']["Surface Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse widening']["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input = data['reverse widening']["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse widening']["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['reverse widening']["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input = data['reverse widening']["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data['reverse widening']["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input = data['reverse widening']["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['reverse widening']["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
        self.layout.add_widget(embed)

        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def pavement_config_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement Configuration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement Configuration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Contiguous or Log Direction of Divided Highway",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Left Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Aux Lane Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Left Aux Lane Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Left Aux Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Left Aux Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Left Aux Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Thru Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Thru Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Through Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['cont or log dir']["Through Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Through Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Aux Lane Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Aux Lane Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Aux Lane Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Aux Lane Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Aux Lane Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Right Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['cont or log dir']["Right Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['cont or log dir']["Right Curb"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.75,'y':0},the_input = data['cont or log dir']["Right Curb"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Total Paved Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Inventory Month-Year:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['cont or log dir']["Total Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data['cont or log dir']["Inventory Month"]+"-"+data['cont or log dir']['Inventory Year'],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Reverse Direction of a Divided Highway",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Left Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Aux Lane Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Left Aux Lane Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Left Aux Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['rev dir div']["Left Aux Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Left Aux Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Thru Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Thru Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Through Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data['rev dir div']["Through Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Through Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Aux Lane Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Aux Lane Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Aux Lane Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Aux Lane Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Aux Lane Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Right Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Right Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Right Curb"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.75,'y':0},the_input = data['rev dir div']["Right Curb"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Median Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Median Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data['rev dir div']["Median Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),hpms_median_type=True,pos_hint={"x":.084,'y':0},the_input = data['rev dir div']["Median Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data['rev dir div']["Median Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)



        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)


    def tiepoints_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Tiepoints"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Tiepoints",font_size = 20,font_name="Arial",color = (1,.5,0,1)))


        num_tiepoints = 1
        for k,v in data.items():
            embed = GridLayout(cols=1,size_hint=(1,1))
            label = Label(text="Tiepoint"+" "+str(num_tiepoints),font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            new_desc = ""
            if k[:-2] in data:
                new_desc=k[:-2]
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = new_desc,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)
            else:
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = k,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Route:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Ramp or TR #",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersection Route"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=75))
            embed.add_widget(TextInput(text = data[k]["Ramp or TR #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
            #lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
            #embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Town:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Intersecting Road",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Road Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersecting Town"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.084,'y':0},the_input = data[k]["Intersecting Town"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Intersecting Road"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Road Class"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Road Class"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Connector:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Connector Seq.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="One Way:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Connector"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Connector Seq."],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["One Way"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),one_way=True,pos_hint={"x":.75,'y':0},the_input =data[k]["One Way"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Tiepoint Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Tiepoint Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Prefix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Tiepoint Code"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_code=True,pos_hint={"x":.084,'y':0},the_input = data[k]["Tiepoint Code"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Tiepoint Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_type=True,pos_hint={"x":.417,'y':0},the_input =data[k]["Tiepoint Type"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Bridge Prefix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_prefix=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Bridge Prefix"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Bridge Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Location:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Bridge Number"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
            embed.add_widget(TextInput(text = data[k]["Bridge Suffix"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Bridge Location"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_location=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Bridge Location"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Exit #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Exit Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Pole Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Exit #"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["Exit Suffix"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["Pole #"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Interchange:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="ATR #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="RR Crossing #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =data[k]["Interchange"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = "",pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["RR Crossing #"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="ADT Break:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Angle:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="HW Log Codes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["ADT Break"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text =data[k]["Angle"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["HW Log Codes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),hw_log_code=True,pos_hint={"x":.75,'y':0},the_input =data[k]["HW Log Codes"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)
            
# go back here


            num_tiepoints+=1


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

        
        

    def get_all_stuff(self,*args):
        self.all_data = get_rest_of_data_sis(self.route,milepoint_formatter(self.milepoint),self.df)
    
    def get_top_stuff(self,*args):
        self.top_stuff = get_top_data_sis(self.main_route_button.text,self.df)

    def search_get_top_stuff(self,*args):
        self.top_stuff = get_top_data_sis(self.cust_route_input.text,self.df)

    def set_milepoint(self,*args):
        self.milepoint = self.main_milepoint_button.text

    def set_route(self,*args):
        self.route = self.main_route_button.text

    def search_clicked_set_route(self,*args):
        self.main_route_button.text = self.cust_route_input.text
        self.route = self.cust_route_input.text

    def search_clicked_set_milepoint(self,*args):
        self.main_milepoint_button.text = self.cust_milepoint_input.text
        self.milepoint = self.cust_milepoint_input.text

    def insert_log_direction(self,*args):
        if self.top_stuff is not None:
            self.log_direction_input.text = self.top_stuff['Log Direction']

    def insert_inv_month(self,*args):
        if self.top_stuff is not None:
            self.inv_month_input.text = self.top_stuff['Inventory Month']

    def insert_inv_year(self,*args):
        if self.top_stuff is not None:
            self.inv_year_input.text = self.top_stuff['Inventory Year']
    
    def prev_page(self,instance):
        self.clear_widgets()
        self.manager.current = "title"

#####################################################################################################################################

class RampsScreen(Screen):
    def __init__(self, **kwargs):
        super(RampsScreen, self).__init__(**kwargs)

    def on_enter(self):
        self.df = create_ramps_df(ramps_ascii_path)
        self.unique_routes = get_unique_routes_ramps(self.df)
        self.unique_ramps=None
        self.unique_milepoints = None
        self.ramp = None
        self.top_stuff = None
        self.route = None
        self.milepoint = None
        self.all_data = None

        self.cust_route_label = Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.953})
        self.add_widget(self.cust_route_label)

        self.cust_route_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.1,'y':.95},font_size = 12)
        self.add_widget(self.cust_route_input)

        self.cust_ramp_label = Label(text="Ramp:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.15,'y':.953})
        self.add_widget(self.cust_ramp_label)

        self.cust_ramp_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.23,'y':.95},font_size = 12)
        self.add_widget(self.cust_ramp_input)

        self.cust_milepoint_label = Label(text="Milepoint:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.345,'y':.953})
        self.add_widget(self.cust_milepoint_label)

        self.cust_milepoint_input = TextInput(multiline=False,size_hint=(.06,.04),pos_hint={'x':.44,'y':.95},font_size = 12)
        self.add_widget(self.cust_milepoint_input)

        self.search_button = Button(text="Search",size_hint=(.14,.04),pos_hint={'x':.55,'y':.95})

        
        self.search_button.bind(on_press=self.create_options)
        self.search_button.bind(on_press=self.search_clicked_set_milepoint)
        self.search_button.bind(on_press=self.create_milepoints)
        self.search_button.bind(on_press=self.search_clicked_set_ramp)
        self.search_button.bind(on_press=self.create_ramps)
        self.search_button.bind(on_press=self.search_clicked_set_route)


        self.add_widget(self.search_button)

        self.first_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.82})
        self.add_widget(self.first_page_line)

        
        self.route_dropdown = DropDown()
        for route in self.unique_routes:
            self.route_button = Button(text=route,size_hint_y = None, height = 20)
            self.route_button.bind(on_release=lambda route_button: self.route_dropdown.select(route_button.text))
            self.route_dropdown.add_widget(self.route_button)

        self.main_route_button = Button(text="Choose Route",size_hint=(.14,.04),pos_hint={'x':.1,'y':.9})
        self.main_route_button.bind(on_release=self.route_dropdown.open)

        self.route_dropdown.bind(on_select=self.create_ramps)
        self.route_dropdown.bind(on_select=self.set_route)
        self.route_dropdown.bind(on_select=lambda instance, x: setattr(self.main_route_button,'text',x))
        self.add_widget(self.main_route_button)

        self.route_label=Label(text="Route:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.903})
        self.add_widget(self.route_label)
        
        self.btn2 = Button(text="Go Home",size_hint=(.1,.05),pos_hint={'x':.45,'y':.03})
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.prev_page)

    def create_ramps(self,*args):
        if self.route is not None:
            try:
                self.remove_widget(self.ramps_dropdown)
                self.ramps_formatter()
            except AttributeError:
                self.ramps_formatter()

    
    def ramps_formatter(self,*args):
        unique_ramps = get_unique_ramps_display(self.route,self.df)
        self.unique_ramps = unique_ramps
        
        self.ramps_dropdown=DropDown()
        for ramp in self.unique_ramps:
            self.ramp_button = Button(text=ramp,size_hint_y = None, height = 20)
            self.ramp_button.bind(on_release=lambda ramp_button: self.ramps_dropdown.select(ramp_button.text))
            self.ramps_dropdown.add_widget(self.ramp_button)
        self.main_ramp_button = Button(text="Choose Ramp",size_hint=(.20,.04),pos_hint={'x':.32,'y':.9})
        self.main_ramp_button.bind(on_release=self.ramps_dropdown.open)

        self.ramps_dropdown.bind(on_select=self.create_milepoints)
        self.ramps_dropdown.bind(on_select=self.set_ramp)
        self.ramps_dropdown.bind(on_select=lambda instance, x: setattr(self.main_ramp_button,'text',x))
                

        self.add_widget(self.main_ramp_button)
        self.ramp_label=Label(text="Ramp:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.217,'y':.903})
        self.add_widget(self.ramp_label)

    def create_milepoints(self,*args):
         if self.ramp is not None:
            try:
                self.remove_widget(self.milepoint_dropdown)
                self.remove_widget(self.road_type_label)
                self.remove_widget(self.road_type_input)
                self.remove_widget(self.cum_miles_input)
                self.remove_widget(self.cum_miles_label)
                self.remove_widget(self.road_direction_input)
                self.remove_widget(self.road_direction_label)
                self.remove_widget(self.road_class_input)
                self.remove_widget(self.road_class_label)
                self.remove_widget(self.road_status_input)
                self.remove_widget(self.road_status_label)
                self.remove_widget(self.ramp_loc_input)
                self.remove_widget(self.ramp_loc_label)
                self.remove_widget(self.inv_year_input)
                self.remove_widget(self.inv_year_label)
                self.remove_widget(self.second_line)
                self.milepoints_formatter()
            except AttributeError:
                self.milepoints_formatter()

    def milepoints_formatter(self,*args):
        self.top_stuff = get_top_data_ramps(self.route,self.ramp,self.df)
        
        self.unique_milepoints = get_unique_mp_per_route_per_ramp(self.route,self.ramp,self.df)

        self.milepoint_dropdown=DropDown()
        for milepoint in self.unique_milepoints:
            self.milepoint_button = Button(text=str(float(milepoint[:3]+'.'+milepoint[3:])),size_hint_y = None, height = 20)
            self.milepoint_button.bind(on_release=lambda milepoint_button: self.milepoint_dropdown.select(milepoint_button.text))
            self.milepoint_dropdown.add_widget(self.milepoint_button)
        self.main_milepoint_button = Button(text="Choose Milepoint",size_hint=(.20,.04),pos_hint={'x':.43,'y':.62})
        self.main_milepoint_button.bind(on_release=self.milepoint_dropdown.open)

        self.milepoint_dropdown.bind(on_select=self.create_options)
        self.milepoint_dropdown.bind(on_select=self.set_milepoint)
        self.milepoint_dropdown.bind(on_select=lambda instance, x: setattr(self.main_milepoint_button,'text',x))

        self.add_widget(self.main_milepoint_button)
        self.milepoint_label=Label(text="Milepoint:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.317,'y':.623})
        self.add_widget(self.milepoint_label)  

        self.road_type_label = Label(text="Road Type:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.04,'y':.823})
        self.add_widget(self.road_type_label)
        self.road_type_input = TextInput(text = self.top_stuff["Road Type"],multiline=False,size_hint=(.05,.04),pos_hint={'x':.14,'y':.82},font_size = 12)
        self.add_widget(self.road_type_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_type=True,pos_hint={"x":.19,'y':.82},the_input =self.top_stuff["Road Type"])
        self.add_widget(lookup)

        self.cum_miles_label = Label(text="Rt.Cum Miles:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.24,'y':.823})
        self.add_widget(self.cum_miles_label)
        self.cum_miles_input = TextInput(text = self.top_stuff["Rt. Cum Miles"],multiline=False,size_hint=(.1,.04),pos_hint={'x':.36,'y':.82},font_size = 12)
        self.add_widget(self.cum_miles_input)

        self.road_direction_label = Label(text="Rt. Direction:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.5,'y':.823})
        self.add_widget(self.road_direction_label)
        self.road_direction_input = TextInput(text = self.top_stuff["Rt. Direction"],multiline=False,size_hint=(.05,.04),pos_hint={'x':.61,'y':.82},font_size = 12)
        self.add_widget(self.road_direction_input)

        self.road_class_label = Label(text="Road Class:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.8,'y':.723})
        self.add_widget(self.road_class_label)
        self.road_class_input = TextInput(text = self.top_stuff["Road Class"],multiline=False,size_hint=(.05,.04),pos_hint={'x':.91,'y':.72},font_size = 12)
        self.add_widget(self.road_class_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.97,'y':.72},the_input =self.top_stuff["Road Class"])
        self.add_widget(lookup)

        self.road_status_label = Label(text="Road Status:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.8,'y':.823})
        self.add_widget(self.road_status_label)
        self.road_status_input = TextInput(text = self.top_stuff["Road Status"],multiline=False,size_hint=(.05,.04),pos_hint={'x':.91,'y':.82},font_size = 12)
        self.add_widget(self.road_status_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),road_status=True,pos_hint={"x":.97,'y':.82},the_input =self.top_stuff["Road Status"])
        self.add_widget(lookup)

        self.ramp_loc_label = Label(text="Ramp Location:",font_size = 16,size_hint=(.1,.04),font_name="Arial",pos_hint={'x':.05,'y':.723})
        self.add_widget(self.ramp_loc_label)
        self.ramp_loc_input = TextInput(text = self.top_stuff["Ramp Location"],multiline=False,size_hint=(.23,.04),pos_hint={'x':.19,'y':.72},font_size = 12)
        self.add_widget(self.ramp_loc_input)

        self.inv_year_label = Label(text="Inventory Month-Year:",font_size = 16,size_hint=(.16,.04),font_name="Arial",pos_hint={'x':.46,'y':.723})
        self.add_widget(self.inv_year_label)
        self.inv_year_input = TextInput(text = self.top_stuff["Inventory Month"]+" "+self.top_stuff["Inventory Year"],multiline=False,size_hint=(.1,.04),pos_hint={'x':.66,'y':.72},font_size = 12)
        self.add_widget(self.inv_year_input)

        self.second_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.63})
        self.add_widget(self.second_line)
                
    def create_options(self,*args):
        if self.milepoint is not None:
            
            try:
                self.remove_widget(self.administration_button)
                self.remove_widget(self.pavement_button)
                self.remove_widget(self.pavconfig_button)
                self.remove_widget(self.tiepoints_button)
                self.remove_widget(self.town_input)
                self.remove_widget(self.town_label)
                self.remove_widget(self.longitude_input)
                self.remove_widget(self.longitude_label)
                self.remove_widget(self.latitude_input)
                self.remove_widget(self.latitude_label)

                self.options_formatter()


            except AttributeError:
                self.options_formatter()

    def options_formatter(self,*args):
        #buttons
        self.all_data = get_rest_of_data_ramps(self.route,self.ramp,milepoint_formatter(self.milepoint),self.df)
       
        self.administration_button = Button(text="View Administration",size_hint=(.20,.04),pos_hint={'x':.02,'y':.4})
        self.administration_button.bind(on_press=self.administration_button_clicked)
        self.add_widget(self.administration_button)

        self.pavement_button = Button(text="View Pavement",size_hint=(.20,.04),pos_hint={'x':.02,'y':.3})
        self.pavement_button.bind(on_press=self.pavement_button_clicked)
        self.add_widget(self.pavement_button)

        self.pavconfig_button = Button(text="View Pavement Config.",size_hint=(.20,.04),pos_hint={'x':.02,'y':.2})
        self.pavconfig_button.bind(on_press=self.pavement_config_button_clicked)
        self.add_widget(self.pavconfig_button)

        self.tiepoints_button = Button(text="View Tiepoints",size_hint=(.20,.04),pos_hint={'x':.02,'y':.1})
        self.tiepoints_button.bind(on_press=self.tiepoints_button_clicked)
        self.add_widget(self.tiepoints_button)

        self.town_label = Label(text="Town:",font_size = 16,size_hint=(.1,.04),font_name="Arial",pos_hint={'x':.05,'y':.553})
        self.add_widget(self.town_label)
        self.town_input = TextInput(text = self.all_data["Top"]["Town"],multiline=False,size_hint=(.07,.04),pos_hint={'x':.15,'y':.55},font_size = 12)
        self.add_widget(self.town_input)

        lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.23,'y':.55},the_input =self.all_data["Top"]["Town"])
        self.add_widget(lookup)

        self.latitude_label = Label(text="Latitude:",font_size = 16,size_hint=(.1,.04),font_name="Arial",pos_hint={'x':.25,'y':.553})
        self.add_widget(self.latitude_label)
        self.latitude_input = TextInput(text = self.all_data["Top"]["Latitude"],multiline=False,size_hint=(.19,.045),pos_hint={'x':.35,'y':.55},font_size = 12)
        self.add_widget(self.latitude_input)

        self.longitude_label = Label(text="Longitude:",font_size = 16,size_hint=(.1,.04),font_name="Arial",pos_hint={'x':.6,'y':.553})
        self.add_widget(self.longitude_label)
        self.longitude_input = TextInput(text = self.all_data["Top"]["Longitude"],multiline=False,size_hint=(.19,.045),pos_hint={'x':.72,'y':.55},font_size = 12)
        self.add_widget(self.longitude_input)

    def administration_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Administration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Administration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=2,size_hint=(1,1))
        label = Label(text="Ramp Description:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        embed.add_widget(TextInput(text = data["Ramp Description"],multiline=False,font_size = 12,size_hint_x=None,width=250))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="NHS:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Fed Aid:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Urban Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Nhs"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Federal Aid"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),fed_aid=True,pos_hint={"x":.417,'y':0},the_input = data["Federal Aid"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Urban Area"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),urban_area=True,pos_hint={"x":.75,'y':0},the_input = data["Urban Area"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="R/U Designation:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Funct. Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Admin System:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Rural Urban Designation"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),r_u_designation=True,pos_hint={"x":.084,'y':0},the_input = data["Rural Urban Designation"].lstrip().rstrip())
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Functional Class"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),functional_class=True,pos_hint={"x":.417,'y':0},the_input = data["Functional Class"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Admin System"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),admin_system=True,pos_hint={"x":.75,'y':0},the_input = data["Admin System"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Reverse Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Log Lanes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Highway Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Reverse Lanes"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["Log Lanes"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        embed.add_widget(TextInput(text = data["Highway Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
        lookup = Lookup(size_hint=(None,None),size=(20,20),highway_type=True,pos_hint={"x":.75,'y':0},the_input = data["Highway Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="On System Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["On System Year"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Adt"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
        embed.add_widget(TextInput(text = data["Adt Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def pavement_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement"]
      

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Ramp Pavement",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Section Length:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =str(data["Ramp Pavement"]["Section Length"]),pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["Ramp Pavement"]["Paved Width"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Pavement Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.75,'y':0},the_input = data["Ramp Pavement"]["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Pavement Surface:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Pavement Surface"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input = data["Ramp Pavement"]["Pavement Surface"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input =data["Ramp Pavement"]["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input =data["Ramp Pavement"]["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input =data["Ramp Pavement"]["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["State Project"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Maint. Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Maint. Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Maint Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),maint_type=True,pos_hint={"x":.084,'y':0},the_input =data["Ramp Pavement"]["Maint Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Ramp Pavement"]["Maint Year"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=1,size_hint=(1,1))
        label = Label(text="Widened Ramp Pavement",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Paved Width:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Widened Ramp Pavement"]["Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Widened Ramp Pavement"]["Pavement Type"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),pavement_type=True,pos_hint={"x":.417,'y':0},the_input =data["Widened Ramp Pavement"]["Pavement Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Pavement Surface:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Base Thickness:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Pavement Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Widened Ramp Pavement"]["Pavement Surface"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),surface_thickness=True,pos_hint={"x":.084,'y':0},the_input =  data["Widened Ramp Pavement"]["Pavement Surface"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Widened Ramp Pavement"]["Base Thickness"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),base_thickness=True,pos_hint={"x":.417,'y':0},the_input =data["Widened Ramp Pavement"]["Base Thickness"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Widened Ramp Pavement"]["Pavement Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Improve Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Improve Loc.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="State Project:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Widened Ramp Pavement"]["Improve Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_type=True,pos_hint={"x":.084,'y':0},the_input =  data["Widened Ramp Pavement"]["Improve Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Widened Ramp Pavement"]["Improve Loc"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),improve_location=True,pos_hint={"x":.417,'y':0},the_input =data["Widened Ramp Pavement"]["Improve Loc"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = "",pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)
    


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def pavement_config_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement Configuration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement Configuration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Left Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Left Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Left Aux. Lane Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.75,'y':0},the_input = data["Left Aux. Lane Type"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Aux. Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data["Left Aux. Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data["Left Aux. Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Thru Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Thru Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Through Lane Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =  data["Through Lane Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input = data["Through Lane Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Aux. Lane Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Right Aux. Lane Type"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),aux_lane_type=True,pos_hint={"x":.084,'y':0},the_input = data["Right Aux. Lane Type"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Right Aux. Lane Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Aux. Lane Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Right Aux. Lane Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Right Aux. Lane Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Right Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Shoulder Pavement:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Right Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Right Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Right Curb"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.75,'y':0},the_input = data["Right Curb"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Total Paved Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Inventory Month-Year:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Total Paved Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["Iventory Month"]+"-"+data['Inventory Year'],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
        self.layout.add_widget(embed)


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def tiepoints_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Tiepoints"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Tiepoints",font_size = 20,font_name="Arial",color = (1,.5,0,1)))

        num_tiepoints = 1
        for k,v in data.items():
            embed = GridLayout(cols=1,size_hint=(1,1))
            label = Label(text="Tiepoint"+" "+str(num_tiepoints),font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            new_desc = ""
            if k[:-2] in data:
                new_desc=k[:-2]
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = new_desc,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)
            else:
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = k,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Route:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Ramp or TR #",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersection Route"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=75))
            embed.add_widget(TextInput(text = data[k]["Ramp or TR #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=35))
            #lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
            #embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Town:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Intersecting Road",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Road Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersecting Town"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.084,'y':0},the_input = data[k]["Intersecting Town"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Intersecting Road"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Road Class"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),road_class=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Road Class"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="One Way:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Tiepoint Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Tiepoint Type:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["One Way"],pos_hint={"x":.0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),one_way=True,pos_hint={"x":.084,'y':0},the_input =data[k]["One Way"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Tiepoint Code"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_code=True,pos_hint={"x":.417,'y':0},the_input = data[k]["Tiepoint Code"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text = data[k]["Tiepoint Type"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_type=True,pos_hint={"x":.75,'y':0},the_input =data[k]["Tiepoint Type"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Bridge Prefix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Bridge Prefix"],pos_hint={"x":.0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_prefix=True,pos_hint={"x":.084,'y':0},the_input =data[k]["Bridge Prefix"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text =data[k]["Bridge Number"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=70))
            embed.add_widget(TextInput(text = data[k]["Bridge Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Bridge Location:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Exit #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Exit Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Bridge Location"],pos_hint={"x":.0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),bridge_location=True,pos_hint={"x":.084,'y':0},the_input =data[k]["Bridge Location"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text =data[k]["Exit #"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text = data[k]["Exit Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Pole #:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Angle:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="HW Log Codes:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Pole #"],pos_hint={"x":.0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text =data[k]["Angle"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["HW Log Codes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),hw_log_code=True,pos_hint={"x":.75,'y':0},the_input =data[k]["HW Log Codes"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)
          

            num_tiepoints+=1


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def search_clicked_set_route(self,*args):
        self.main_route_button.text = self.cust_route_input.text
        self.route = self.cust_route_input.text

    def search_clicked_set_ramp(self,*args):
        self.main_ramp_button.text = self.cust_ramp_input.text
        self.ramp = self.cust_ramp_input.text

    def search_clicked_set_milepoint(self,*args):
        self.main_milepoint_button.text = self.cust_milepoint_input.text
        self.milepoint = self.cust_milepoint_input.text

    def set_milepoint(self,*args):
        self.milepoint = self.main_milepoint_button.text

    def set_ramp(self,*args):
        self.ramp = self.main_ramp_button.text

    def set_route(self,*arags):
        self.route=self.main_route_button.text

    def prev_page(self,instance):
        self.clear_widgets()
        self.manager.current = "title"

######################################################################################################################################
    
class TownScreen(Screen):
    def __init__(self, **kwargs):
        super(TownScreen, self).__init__(**kwargs)
    
    def on_enter(self):
        self.df = create_town_df(town_ascii_path)
        self.unique_towns = get_unique_towns(self.df)
        self.unique_roads = None
        self.unique_milepoints = None
        self.road = None
        self.town = None
        self.milepoint = None
        self.top_stuff=None
        self.all_data = None

        self.cust_town_label = Label(text="Town:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.953})
        self.add_widget(self.cust_town_label)

        self.cust_town_input = TextInput(multiline=False,size_hint=(.05,.04),pos_hint={'x':.1,'y':.95},font_size = 12)
        self.add_widget(self.cust_town_input)

        self.cust_road_label = Label(text="Road:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.15,'y':.953})
        self.add_widget(self.cust_road_label)

        self.cust_road_input = TextInput(multiline=False,size_hint=(.1,.04),pos_hint={'x':.23,'y':.95},font_size = 12)
        self.add_widget(self.cust_road_input)

        self.cust_milepoint_label = Label(text="Milepoint:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.345,'y':.953})
        self.add_widget(self.cust_milepoint_label)

        self.cust_milepoint_input = TextInput(multiline=False,size_hint=(.06,.04),pos_hint={'x':.44,'y':.95},font_size = 12)
        self.add_widget(self.cust_milepoint_input)

        self.search_button = Button(text="Search",size_hint=(.14,.04),pos_hint={'x':.55,'y':.95})

        self.search_button.bind(on_press=self.create_options)
        self.search_button.bind(on_press=self.search_clicked_set_milepoint)
        self.search_button.bind(on_press=self.create_milepoints)
        self.search_button.bind(on_press=self.search_clicked_set_road)
        self.search_button.bind(on_press=self.create_roads)
        self.search_button.bind(on_press=self.search_clicked_set_town)

        self.add_widget(self.search_button)

        self.first_page_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.82})
        self.add_widget(self.first_page_line)

        self.town_dropdown = DropDown()
        for town in self.unique_towns:
            self.town_button = Button(text=town,size_hint_y = None, height = 20)
            self.town_button.bind(on_release=lambda town_button: self.town_dropdown.select(town_button.text))
            self.town_dropdown.add_widget(self.town_button)

        self.main_town_button = Button(text="Choose Town",size_hint=(.14,.04),pos_hint={'x':.1,'y':.9})
        self.main_town_button.bind(on_release=self.town_dropdown.open)

        self.town_dropdown.bind(on_select=self.create_roads)
        self.town_dropdown.bind(on_select=self.set_town)
        self.town_dropdown.bind(on_select=lambda instance, x: setattr(self.main_town_button,'text',x))
        self.add_widget(self.main_town_button)

        self.route_label=Label(text="Town:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.02,'y':.903})
        self.add_widget(self.route_label)



        self.btn2 = Button(text="Go Home",size_hint=(.1,.05),pos_hint={'x':.45,'y':.03})
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.prev_page)

    def create_roads(self,*args):
        if self.town is not None:
            try:
                self.remove_widget(self.roads_dropdown)
                self.remove_widget(self.road_label)
                self.roads_formatter()
            except AttributeError:
                self.roads_formatter()

    def roads_formatter(self,*args):
        unique_roads = get_unique_routes_per_town(self.town,self.df)
        self.unique_roads=unique_roads

        self.roads_dropdown=DropDown()
        for road in self.unique_roads:
            self.road_button = Button(text=road,size_hint_y = None, height = 20)
            self.road_button.bind(on_release=lambda road_button: self.roads_dropdown.select(road_button.text))
            self.roads_dropdown.add_widget(self.road_button)
        self.main_road_button = Button(text="Choose Road",size_hint=(.3,.04),pos_hint={'x':.35,'y':.9})
        self.main_road_button.bind(on_release=self.roads_dropdown.open)

        self.roads_dropdown.bind(on_select=self.create_milepoints)
        self.roads_dropdown.bind(on_select=self.set_road)
        self.roads_dropdown.bind(on_select=lambda instance, x: setattr(self.main_road_button,'text',x))
                

        self.add_widget(self.main_road_button)
        self.road_label=Label(text="Road:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.217,'y':.903})
        self.add_widget(self.road_label)

    def create_milepoints(self,*arags):
        if self.road is not None:
            try:
                self.remove_widget(self.milepoint_dropdown)
                self.remove_widget(self.milepoint_label) 
                self.remove_widget(self.road_name_input)
                self.remove_widget(self.road_name_label)
                self.remove_widget(self.direction_input)
                self.remove_widget(self.direction_label)
                self.remove_widget(self.grid_input)
                self.remove_widget(self.grid_label)
                self.remove_widget(self.grid_num_input)
                self.remove_widget(self.grid_num_label)
                self.remove_widget(self.second_line)
                self.milepoints_formatter()
            except AttributeError:
                self.milepoints_formatter()

    def milepoints_formatter(self,*args):
        self.top_stuff = get_top_data_town(self.town,self.road,self.df)
        self.unique_milepoints = get_unique_mp_per_route_per_town(self.town,self.road,self.df)

        self.milepoint_dropdown=DropDown()
        for milepoint in self.unique_milepoints:
            if len(milepoint.rstrip())!=0:
                self.milepoint_button = Button(text=str(float(milepoint[:3]+'.'+milepoint[3:])),size_hint_y = None, height = 20)
                self.milepoint_button.bind(on_release=lambda milepoint_button: self.milepoint_dropdown.select(milepoint_button.text))
                self.milepoint_dropdown.add_widget(self.milepoint_button)
        self.main_milepoint_button = Button(text="Choose Milepoint",size_hint=(.20,.04),pos_hint={'x':.43,'y':.62})
        self.main_milepoint_button.bind(on_release=self.milepoint_dropdown.open)

        self.milepoint_dropdown.bind(on_select=self.create_options)
        self.milepoint_dropdown.bind(on_select=self.set_milepoint)
        self.milepoint_dropdown.bind(on_select=lambda instance, x: setattr(self.main_milepoint_button,'text',x))

        self.add_widget(self.main_milepoint_button)
        self.milepoint_label=Label(text="Milepoint:",font_size = 16,size_hint=(.12,.04),font_name="Arial",pos_hint={'x':.317,'y':.623})
        self.add_widget(self.milepoint_label) 

        self.road_name_label = Label(text="Road Name:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.823})
        self.add_widget(self.road_name_label)
        self.road_name_input = TextInput(text = self.top_stuff["Road Name"],multiline=False,size_hint=(.2,.04),pos_hint={'x':.17,'y':.82},font_size = 12)
        self.add_widget(self.road_name_input)

        self.direction_label = Label(text="Direction:",font_size = 16,size_hint=(.08,.05),font_name="Arial",pos_hint={'x':.45,'y':.823})
        self.add_widget(self.direction_label)
        self.direction_input = TextInput(text = self.top_stuff["Direction"],multiline=False,size_hint=(.1,.04),pos_hint={'x':.55,'y':.82},font_size = 12)
        self.add_widget(self.direction_input)

        self.grid_label = Label(text="Grid Letter:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.723})
        self.add_widget(self.grid_label)
        self.grid_input = TextInput(text = self.top_stuff["Grid_Letter"],multiline=False,size_hint=(.05,.05),pos_hint={'x':.17,'y':.72},font_size = 12)
        self.add_widget(self.grid_input)

        self.grid_num_label = Label(text="Grid Number:",font_size = 16,size_hint=(.08,.05),font_name="Arial",pos_hint={'x':.45,'y':.723})
        self.add_widget(self.grid_num_label)
        self.grid_num_input = TextInput(text = self.top_stuff["Grid_Number"],multiline=False,size_hint=(.05,.05),pos_hint={'x':.57,'y':.725},font_size = 12)
        self.add_widget(self.grid_num_input)

        self.second_line = Label(text = "____________________________________________________________________________________________________",font_size=30,size_hint=(1,None),pos_hint={'x':0,'y':.63})
        self.add_widget(self.second_line)
    
    def create_options(self,*args):
        if self.milepoint is not None:
            
            try:
                self.remove_widget(self.administration_button)
                self.remove_widget(self.pavconfig_button)
                self.remove_widget(self.tiepoints_button)
                self.remove_widget(self.latitude_label)
                self.remove_widget(self.latitude_input)
                self.remove_widget(self.longitude_input)
                self.remove_widget(self.longitude_label)
                self.remove_widget(self.node_code_label)
                self.remove_widget(self.node_code_input)
                self.remove_widget(self.node_number_input)
                self.remove_widget(self.node_number_label)

                self.options_formatter()


            except AttributeError:
                self.options_formatter()

    def options_formatter(self,*args):
        #buttons
        self.all_data = get_rest_of_data_town(self.town,self.road,milepoint_formatter(self.milepoint),self.df)
       
        self.administration_button = Button(text="View Administration",size_hint=(.20,.04),pos_hint={'x':.02,'y':.3})
        self.administration_button.bind(on_press=self.administration_button_clicked)
        self.add_widget(self.administration_button)

        self.pavconfig_button = Button(text="View Pavement Config.",size_hint=(.20,.04),pos_hint={'x':.02,'y':.2})
        self.pavconfig_button.bind(on_press=self.pavement_config_button_clicked)
        self.add_widget(self.pavconfig_button)

        self.tiepoints_button = Button(text="View Tiepoints",size_hint=(.20,.04),pos_hint={'x':.02,'y':.1})
        self.tiepoints_button.bind(on_press=self.tiepoints_button_clicked)
        self.add_widget(self.tiepoints_button)

        self.latitude_label = Label(text="Latitude:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.573})
        self.add_widget(self.latitude_label)
        self.latitude_input = TextInput(text = self.all_data["Top"]["Latitude"],multiline=False,size_hint=(.2,.04),pos_hint={'x':.15,'y':.57},font_size = 12)
        self.add_widget(self.latitude_input)

        self.longitude_label = Label(text="Longitude:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.05,'y':.503})
        self.add_widget(self.longitude_label)
        self.longitude_input = TextInput(text = self.all_data["Top"]["Latitude"],multiline=False,size_hint=(.2,.04),pos_hint={'x':.15,'y':.5},font_size = 12)
        self.add_widget(self.longitude_input)

        self.node_number_label = Label(text="Node Number:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.63,'y':.573})
        self.add_widget(self.node_number_label)
        self.node_number_input = TextInput(text = self.all_data["Top"]["Node Number"],multiline=False,size_hint=(.2,.04),pos_hint={'x':.77,'y':.57},font_size = 12)
        self.add_widget(self.node_number_input)

        self.node_code_label = Label(text="Node Code:",font_size = 16,size_hint=(.08,.04),font_name="Arial",pos_hint={'x':.63,'y':.503})
        self.add_widget(self.node_code_label)
        self.node_code_input = TextInput(text = self.all_data["Top"]["Node Code"],multiline=False,size_hint=(.2,.04),pos_hint={'x':.77,'y':.5},font_size = 12)
        self.add_widget(self.node_code_input)



    def administration_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Administration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        #self.layout = BoxLayout(size_hint=(1,None),orientation="vertical")
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Administration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))


        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="NHS:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Prefix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["NHS"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["HPMS Prefix"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["HPMS Number"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="HPMS Subdivision:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Month:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="HPMS Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["HPMS Subdivision"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["HPMS Month"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["HPMS Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="ADT Sample:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT Volume:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="ADT Year:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =  data["ADT Sample"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = data["ADT Volume"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=80))
        embed.add_widget(TextInput(text =data["ADT Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Urban Area:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Funct. Class:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="One Way:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =  data["Urban Area"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),urban_area=True,pos_hint={"x":.084,'y':0},the_input =data["Urban Area"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Funct. Class"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),functional_class=True,pos_hint={"x":.417,'y':0},the_input =data["Funct. Class"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["One Way"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),one_way=True,pos_hint={"x":.75,'y':0},the_input =data["One Way"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)
        


        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def pavement_config_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Pavement Configuration"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Pavement Configuration",font_size = 20,font_name="Arial",color = (1,.5,0,1)))


        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Outside Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input = data["Left Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =  data["Left Outside Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Outside Shoulder Pave.:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Travel Way Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Ouside Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Left Ouside Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Left Travel Way Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Travel Way Pave.:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Left Inside Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text = data["Left Travel Way Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Left Travel Way Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Left Inside Shoulder Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Left Inside Shoulder Pave.:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Total Paved Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Left Inside Shoulder Pavement"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.084,'y':0},the_input = data["Left Inside Shoulder Pavement"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text = data["Total Paved Width"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Median Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Median Type:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Median Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text = "",pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),hpms_median_type=True,pos_hint={"x":.75,'y':0},the_input = "")
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Travel Way Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Travel Way Pave.:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Right Travel Way Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Right Travel Way Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input =data["Right Travel Way Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Outside Shoulder Width:",font_size = 14.5,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Outside Shoulder Pave.:",font_size = 14.5,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Right Ouside Shoulder Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Right Outside Shoulder Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input =data["Right Outside Shoulder Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Inside Shoulder Width:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Right Inside Shoulder Pave.:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Right Inside Shoulder Width"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        embed.add_widget(TextInput(text =data["Right Inside Shoulder Pavement"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),shoulder_pavement=True,pos_hint={"x":.75,'y':0},the_input =data["Right Inside Shoulder Pavement"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="Right Curb:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Number of Through Lanes:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["Right Curb"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),curb=True,pos_hint={"x":.084,'y':0},the_input =data["Right Curb"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Number of Through Lanes"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="On System Year:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Rural Urban Code:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["On Sys Year"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
        embed.add_widget(TextInput(text =data["Rural Urban Code"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),rural_urban=True,pos_hint={"x":.75,'y':0},the_input =data["Rural Urban Code"])
        embed.add_widget(lookup)
        self.layout.add_widget(embed)

        embed = GridLayout(cols=3,size_hint=(1,1))
        label = Label(text="System Maintenance:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        label = Label(text="Inventory Year:",font_size = 15,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
        label.bind(size=label.setter('text_size'))
        embed.add_widget(label)
        self.layout.add_widget(embed)

        embed=FloatLayout()
        embed.add_widget(TextInput(text =data["System Maintenance"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        lookup = Lookup(size_hint=(None,None),size=(20,20),system_maintenance=True,pos_hint={"x":.084,'y':0},the_input =data["System Maintenance"])
        embed.add_widget(lookup)
        embed.add_widget(TextInput(text =data["Inventory Year"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
        self.layout.add_widget(embed)

        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def tiepoints_button_clicked(self,*args):
        try: 
            self.remove_widget(self.scroll)
        except AttributeError:
            pass
        data = self.all_data["Tiepoints"]

        self.layout = GridLayout(cols=1,size_hint=(1,None),row_default_height = 27)
        self.layout.bind(minimum_height = self.layout.setter("height"))
        self.layout.add_widget(Label(text="Tiepoints",font_size = 20,font_name="Arial",color = (1,.5,0,1)))
#go here now
        num_tiepoints = 1
        for k,v in data.items():
            
            embed = GridLayout(cols=1,size_hint=(1,1))
            label = Label(text="Tiepoint"+" "+str(num_tiepoints),font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle",color = (0,1,0,1))
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            new_desc = ""
            if k[:-2] in data:
                new_desc=k[:-2]
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = new_desc,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)
            else:
                embed = GridLayout(cols=2,size_hint=(1,1))
                label = Label(text="Intersecting Desc:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
                label.bind(size=label.setter('text_size'))
                embed.add_widget(label)
                embed.add_widget(TextInput(text = k,multiline=False,font_size = 12,size_hint_x=None,width=250))
                self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Intersecting Route:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Intersecting Town:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Intersecting Road:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text = data[k]["Intersecting Route"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            embed.add_widget(TextInput(text =data[k]["Intersecting Town"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            lookup = Lookup(size_hint=(None,None),size=(20,20),town=True,pos_hint={"x":.45,'y':0},the_input =data[k]["Intersecting Town"])
            embed.add_widget(lookup)
            embed.add_widget(TextInput(text =data[k]["Intersecting Road"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=50))
            #lookup = Lookup(size_hint=(None,None),size=(20,20),fc_link=True,pos_hint={"x":.75,'y':0},the_input = data["FC Link"])
            #embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Connector:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Connector Count.:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Tiepoint Code:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =  data[k]["Connector"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text =data[k]["Connector Count"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Tiepoint Code"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            lookup = Lookup(size_hint=(None,None),size=(20,20),tiepoint_code=True,pos_hint={"x":.75,'y':0},the_input =  data[k]["Tiepoint Code"])
            embed.add_widget(lookup)
            self.layout.add_widget(embed)

            embed = GridLayout(cols=3,size_hint=(1,1))
            label = Label(text="Angle:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Number:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            label = Label(text="Bridge Suffix:",font_size = 16,font_name="Arial",size_hint=(1,1),halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            self.layout.add_widget(embed)

            embed=FloatLayout()
            embed.add_widget(TextInput(text =  data[k]["Angle"],pos_hint={"x":0,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            embed.add_widget(TextInput(text = data[k]["Bridge Number"],pos_hint={"x":.333,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=60))
            embed.add_widget(TextInput(text = data[k]["Bridge Suffix"],pos_hint={"x":.666,"y":0},multiline=False,font_size = 12,size_hint_x = None,width=40))
            self.layout.add_widget(embed)

            embed = GridLayout(cols=2,size_hint=(1,1))
            label = Label(text="Leg. Bridge Name:",font_size = 16,font_name="Arial",size_hint=(None,1),width=160,halign="left",valign = "middle")
            label.bind(size=label.setter('text_size'))
            embed.add_widget(label)
            embed.add_widget(TextInput(text = data[k]["Leg. Bridge Name"],multiline=False,font_size = 12,size_hint_x=None,width=250))
            self.layout.add_widget(embed)


            num_tiepoints+=1




        self.scroll = ScrollView(size_hint=(.72,None),size = (800*.65,600*.4),pos_hint={'x':.25,'y':.10})
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def search_clicked_set_town(self,*args):
        self.main_town_button.text = self.cust_town_input.text
        self.town = self.cust_town_input.text

    def search_clicked_set_road(self,*args):
        self.main_road_button.text = self.cust_road_input.text
        self.road = self.cust_road_input.text

    def search_clicked_set_milepoint(self,*args):
        self.main_milepoint_button.text = self.cust_milepoint_input.text
        self.milepoint = self.cust_milepoint_input.text
    

    def set_milepoint(self,*args):
        self.milepoint = self.main_milepoint_button.text 

    def set_road(self,*args):
        self.road = self.main_road_button.text

    def set_town(self,*args):
        self.town = self.main_town_button.text

    def prev_page(self,instance):
        self.clear_widgets()
        self.manager.current = "title"

########################################################################################################################################
#fixed_size = (800,600)
#def reSize(*args):
  #  Window.size = fixed_size
   # return True
#Window.bind(on_maximize=reSize)


class MainApp(App):
    icon = 'ris_log.png'
    title = 'RIS 2.0'
    def build(self):
        Window.clearcolor = (.0234,.0234,.773,1)
        
        
        title_screen = TitleScreen(name="title")
        state_screen = StateScreen(name="state")
        town_screen = TownScreen(name="town")
        ramps_screen = RampsScreen(name="ramps")
        sis_screen = SisScreen(name="sis")

        main = BoxLayout(size_hint=(None,None),size=(800,600),pos_hint = {'center_x':.5,"center_y":.5})

        root = WindowManager(transition=NoTransition())
        root.add_widget(title_screen)
        root.add_widget(state_screen)
        root.add_widget(town_screen)
        root.add_widget(ramps_screen)
        root.add_widget(sis_screen)
        main.add_widget(root)
        return main

if __name__ == "__main__":
    MainApp().run()