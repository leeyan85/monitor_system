var product_arr = new Array("Mobile","TV","Box");
var s_a = new Array();
s_a[0]="";
s_a[1]="Ruby|Lafite|Viper|Connect|Jade";
s_a[2]="Demeter";

var s_a_model=[];
s_a_model["Ruby"]="RUBY_DEV_LEUI";
s_a_model["Lafite"]="LAFITE_DEV_BSP|S2_US_STABLE_022_20170116|S2_US_STABLE_021_20161229|LAFITE_N_DEV_LEUI_LITE|LAFITE_N_DEV_BSP";
s_a_model["Viper"]="VIPER_EVT_BSP";
s_a_model["Connect"]="ZL1_NA_STABLE_022_20170116|ZL1_NA_MP_SHIPPING_20160921";
s_a_model["Jade"]="JADE_DEV_BSP";
s_a_model["Demeter"]="DEMETER_TIF_FINAL";

var s_a_build_type=[];
s_a_build_type["X2"]="Daily";
s_a_build_type["S2"]="Daily";
s_a_build_type["BSP"]="Daily-Factory";

var count_id=0;

function print_product(product_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(product_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select Business','');
	option_str.selectedIndex = 0;
	for (var i=0; i<product_arr.length; i++) {
		option_str.options[option_str.length] = new Option(product_arr[i],product_arr[i]);
	}
}

function print_branch(branch_id, branch_index){
	count_id=branch_index;
	var option_str = document.getElementById(branch_id);
	option_str.length=0;	
	option_str.options[0] = new Option('Select Product','');
	option_str.selectedIndex = 0;
	var branch_arr = s_a[branch_index].split("|");
	for (var i=0; i<branch_arr.length; i++) {
		option_str.options[option_str.length] = new Option(branch_arr[i],branch_arr[i]);
	}
}

function print_model(model_id, model_index){
	var option_str = document.getElementById(model_id);
	option_str.length=0;	
	option_str.options[0] = new Option('Select Branch','');
	var model_arr = s_a_model[model_index].split("|");
	for (var i=0; i<model_arr.length; i++) {
		option_str.options[option_str.length] = new Option(model_arr[i],model_arr[i]);
	}
}
