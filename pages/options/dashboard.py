from streamlit_option_menu import option_menu
from pages.options.dashboard_options.download_stoxx_sheet import download_stoxx_sheet
from pages.options.dashboard_options.fill_timesheet import fill_timesheet
from pages.options.dashboard_options.role_allocation import role_allocation
from pages.options.dashboard_options.timesheet_status import timesheet_status
from pages.options.dashboard_options.upload_data import upload_data_section
from utility.data import project_code_list, project_name_list



def show_dashboard(user_profile):
    """Display the dashboard section with employee details, hours worked, and leave overview."""
    if(user_profile["role"]["is_super_user"]):
        options =["Timesheet Status","Upload Data","Edit Timesheet",
            "Stoxx Sheet","Role Allocation",]
    else:
        options =["Timesheet Status","Upload Data","Edit Timesheet",
            "Stoxx Sheet",]
   
    choice = option_menu(
        menu_title=None,
        options = options,
        icons= ["pie-chart-fill", "upload", "pencil-square", "download", "person-gear"],
      
        default_index=0,
        orientation="horizontal",
    )

    project_code_options = project_code_list()
    project_name_options = project_name_list()


    if choice == "Timesheet Status":
    # with tab1:
        timesheet_status(user_profile['indxx_id'],project_name_options)

    elif choice == "Upload Data":
    # with tab2:
        upload_data_section()

    elif choice == "Edit Timesheet":
    # with tab3:
        fill_timesheet()

    elif choice == "Stoxx Sheet":
    # with tab4:
        download_stoxx_sheet(project_code_options)

    elif choice == "Role Allocation":
    # with tab5:
        role_allocation()