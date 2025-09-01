import streamlit as st


def page1():
    st.write(st.session_state.foo)


def page2():
    st.write(st.session_state.bar)


pages = {
    "App": [
        st.Page("src/intro/intro.py", title="Intro"),
    ],
    "Forms": [
        st.Page("src/forms/form1.py", title="Form  1"),
        st.Page("src/forms/form2.py", title="Form  2"),
        st.Page("src/forms/form_container.py", title="Container"),
        st.Page("src/forms/form_default.py", title="Default"),
        st.Page("src/forms/form_process1.py", title="Process  1"),
        st.Page("src/forms/form_process2.py", title="Process  2"),
        st.Page("src/forms/form_process3.py", title="Process  3"),
        st.Page("src/forms/form_overview.py", title="Overview"),
    ],
    "Widgets": [
        st.Page("src/widget/radio.py", title="Radio"),
        st.Page("src/widget/camera_input.py", title="Camera Input"),
        st.Page(
            "src/widget/multiselect_accept_new_options.py",
            title="Multiselect Accept New Options",
        ),
        st.Page("src/widget/selectbox.py", title="Selectbox"),
        st.Page(
            "src/widget/segmented_control_multi.py", title="Segmented Control Multi"
        ),
        st.Page("src/widget/link_button.py", title="Link Button"),
        st.Page("src/widget/audio_input.py", title="Audio Input"),
        st.Page("src/widget/download_button_csv.py", title="Download Button Csv"),
        st.Page("src/widget/text_area_widget.py", title="Text Area"),
        st.Page("src/widget/radio_empty.py", title="Radio Empty"),
        st.Page("src/widget/date_input_empty.py", title="Date Input Empty"),
        st.Page("src/widget/pills_multi.py", title="Pills Multi"),
        st.Page("src/widget/select_slider.py", title="Select Slider"),
        st.Page("src/widget/toggle.py", title="Toggle"),
        st.Page("src/widget/button_icons.py", title="Button Icons"),
        st.Page("src/widget/checkbox.py", title="Checkbox"),
        st.Page("src/widget/number_input_empty.py", title="Number Input Empty"),
        st.Page(
            "src/widget/segmented_control_single.py", title="Segmented Control Single"
        ),
        st.Page("src/widget/download_button_text.py", title="Download Button Text"),
        st.Page("src/widget/time_input_empty.py", title="Time Input Empty"),
        st.Page("src/widget/date_input.py", title="Date Input"),
        st.Page(
            "src/widget/file_uploader_directory.py", title="File Uploader Directory"
        ),
        st.Page("src/widget/feedback_stars.py", title="Feedback Stars"),
        st.Page("src/widget/selectbox1.py", title="Selectbox  1"),
        st.Page("src/widget/radio1.py", title="Radio  1"),
        st.Page("src/widget/download_button_file.py", title="Download Bbutton"),
        st.Page("src/widget/number_input.py", title="Number Input"),
        st.Page("src/widget/time_input.py", title="Time Input"),
        st.Page("src/widget/selectbox_empty.py", title="Selectbox Empty"),
        st.Page("src/widget/download_button.py", title="Download Button"),
        st.Page("src/widget/page_link/widget.page_link.py", title="Page Link"),
        st.Page("src/widget/button.py", title="Button"),
        st.Page("src/widget/pills_single.py", title="Pills Single"),
        st.Page("src/widget/color_picker.py", title="Color Picker"),
        st.Page("src/widget/multiselect.py", title="Multiselect"),
        st.Page("src/widget/file_uploader.py", title="File Uploader"),
        st.Page("src/widget/feedback_thumbs.py", title="Feedback Thumbs"),
        st.Page("src/widget/slider.py", title="Slider"),
        st.Page("src/widget/date_input1.py", title="Date Input 1"),
        st.Page("src/widget/text_input1.py", title="Text Input 1"),
        st.Page(
            "src/widget/selectbox_accept_new_options.py",
            title="Selectbox Accept New Options",
        ),
        st.Page("src/widget/text_input.py", title="Text Input"),
    ],
    "Chat": [
        st.Page("src/chat/input.py", title="Input"),
        st.Page("src/chat/input_set_value.py", title="Input Set Value"),
        st.Page("src/chat/simple.py", title="Simple"),
        st.Page("src/chat/message.py", title="Message"),
        st.Page("src/chat/input-inline.py", title="Input-inline"),
        st.Page("src/chat/llm.py", title="LLM"),
        st.Page("src/chat/input-file-uploader.py", title="Input File-Uploader"),
        st.Page("src/chat/echo.py", title="Echo"),
    ],
    "Layout": [
        st.Page("src/layout/columns_borders.py", title="Columns Borders"),
        st.Page("src/layout/columns_bottom_widgets.py", title="Columns Bottom Widgets"),
        st.Page(
            "src/layout/columns_vertical_alignment.py",
            title="Columns Vertical Alignment",
        ),
        st.Page("src/layout/columns1.py", title="Columns  1"),
        st.Page("src/layout/columns2.py", title="Columns  2"),
        st.Page("src/layout/container1.py", title="Container  1"),
        st.Page("src/layout/container2.py", title="Container  2"),
        st.Page("src/layout/container3.py", title="Container  3"),
        st.Page("src/layout/container4.py", title="Container  4"),
        st.Page("src/layout/container5.py", title="Container  5"),
        st.Page("src/layout/empty_placeholder.py", title="Empty Placeholder"),
        st.Page("src/layout/empty.py", title="Empty"),
        st.Page("src/layout/expander.py", title="Expander"),
        st.Page("src/layout/popover.py", title="Popover"),
        st.Page("src/layout/popover2.py", title="Popover  2"),
        st.Page("src/layout/tabs1.py", title="Tabs  1"),
        st.Page("src/layout/tabs2.py", title="Tabs  2"),
    ],
    "Navigation": [
        st.Page("src/navigation/navigation.py", title="Navigation"),
    ],
    "Charts": [
        st.Page("src/charts/altair_selections.py", title="Altair Selections"),
        st.Page("src/charts/area_chart_steamgraph.py", title="Area Chart Steamgraph"),
        st.Page("src/charts/area_chart.py", title="Area Chart"),
        st.Page("src/charts/area_chart1.py", title="Area Chart 1"),
        st.Page("src/charts/area_chart2.py", title="Area Chart 2"),
        st.Page("src/charts/audio-purr.py", title="Audio-purr"),
        st.Page("src/charts/audio.py", title="Audio"),
        st.Page("src/charts/bar_chart_horizontal.py", title="Bar Chart Horizontal"),
        st.Page("src/charts/bar_chart_unstacked.py", title="Bar Chart Unstacked"),
        st.Page("src/charts/bar_chart.py", title="Bar Chart"),
        st.Page("src/charts/bar_chart1.py", title="Bar Chart 1"),
        st.Page("src/charts/bar_chart2.py", title="Bar Chart 2"),
        st.Page("src/charts/bokeh_chart.py", title="Bokeh Chart"),
        st.Page("src/charts/graphviz_chart.py", title="Graphviz Chart"),
        st.Page("src/charts/image.py", title="Image"),
        st.Page("src/charts/line_chart.py", title="Line Chart"),
        st.Page("src/charts/line_chart1.py", title="Line Chart 1"),
        st.Page("src/charts/line_chart2.py", title="Line Chart 2"),
        st.Page("src/charts/map_color.py", title="Map Color"),
        st.Page("src/charts/map.py", title="Map"),
        st.Page("src/charts/plotly_chart_config.py", title="Plotly Chart Config"),
        st.Page(
            "src/charts/plotly_chart_event_state_selections.py",
            title="Plotly Chart Event State Selections",
        ),
        st.Page(
            "src/charts/plotly_chart_event_state.py", title="Plotly Chart Event State"
        ),
        st.Page("src/charts/plotly_chart.py", title="Plotly Chart"),
        st.Page("src/charts/pydeck_chart.py", title="Pydeck Chart"),
        st.Page(
            "src/charts/pydeck_event_state_selections.py",
            title="Pydeck Event State Selections",
        ),
        st.Page("src/charts/pyplot.py", title="PyPlot"),
        st.Page("src/charts/scatter_chart.py", title="Scatter Chart"),
        st.Page("src/charts/scatter_chart1.py", title="Scatter Chart 1"),
        st.Page("src/charts/scatter_chart2.py", title="Scatter Chart 2"),
        st.Page("src/charts/vega_lite_chart.py", title="Vega Lite Chart"),
        st.Page("src/charts/video.py", title="Video"),
        st.Page("src/charts/video2.py", title="Video 2"),
        st.Page(
            "src/charts/video3/pages/1_One_VTT_or_SRT_file.py",
            title="Subtitles: One VTT Or SRT File",
        ),
        st.Page(
            "src/charts/video3/pages/2_Multiple_VTT_and_or_SRT_files.py",
            title="Subtitles: Multiple VTT And Or SRT Files",
        ),
        st.Page(
            "src/charts/video3/pages/3_Upload_subtitles.py",
            title="Subtitles: Upload Subtitles",
        ),
        st.Page(
            "src/charts/video3/pages/4_YouTube_is_unsupported.py",
            title="Subtitles: YouTube Is Unsupported",
        ),
        st.Page(
            "src/charts/video3/pages/5_Raw_strings_and_BytesIO.py",
            title="Subtitles: Raw Strings And BytesIO",
        ),
        st.Page(
            "src/charts/video3/pages/6_Playground.py", title="Subtitles: Playground"
        ),
        st.Page("src/charts/video3/video_subtitles.py", title="Subtitles"),
    ],
    "Status": [
        st.Page("src/status/exception.py", title="Exception"),
        st.Page("src/status/progress.py", title="Progress"),
        st.Page("src/status/spinner.py", title="Spinner"),
        st.Page("src/status/status.py", title="Status"),
        st.Page("src/status/status1.py", title="Status 1"),
        st.Page("src/status/toast.py", title="Toast"),
        st.Page("src/status/toast1.py", title="Toast 1"),
        st.Page("src/status/toast2.py", title="Toast 2"),
    ],
    "MPA": [
        st.Page("src/mpa-hello/0_👋_Hello.py", title="👋 Hello"),
    ],
    "Utilities": [
        st.Page("src/utilities/help.py", title="Utilities.help"),
        st.Page(
            "src/utilities/switch_page/utilities.switch_page.py", title="Switch Page"
        ),
        st.Page("src/utilities/help2.py", title="Utilities.help 2"),
        st.Page("src/utilities/html.py", title="Utilities.html"),
        st.Page("src/utilities/help1.py", title="Utilities.help 1"),
    ],
    "Theming": [
        st.Page(
            "src/theming/charts.plotly_custom_colors.py", title="Plotly Custom Colors"
        ),
        st.Page("src/theming/charts.vega_lite_theme.py", title="Vega Lite Theme"),
        st.Page("src/theming/charts.plotly_chart_theme.py", title="Plotly Chart Theme"),
        st.Page(
            "src/theming/charts.altair_custom_colors.py", title="Altair Custom Colors"
        ),
        st.Page("src/theming/charts.altair_chart.py", title="Altair Chart"),
    ],
    "Guides": [
        st.Page(
            "src/guides/widgets.change_parameters_best.py",
            title="Change Parameters Best",
        ),
        st.Page("src/guides/widgets.change_parameters.py", title="Change Parameters"),
        st.Page("src/guides/widgets.form_callbacks.py", title="Form Callbacks"),
    ],
    "Execution": [
        st.Page("src/execution/dialog.py", title="Dialog"),
        st.Page("src/execution/fragment_balloon.py", title="Fragment Balloon"),
        st.Page("src/execution/fragment-rerun.py", title="Fragment ReRun"),
        st.Page("src/execution/fragment.py", title="Execution.fragment"),
    ],
    "Tutorials": [
        st.Page(
            "src/tutorials/customnavigation/custom-navigation.py",
            title="Custom Navigation",
        ),
        st.Page(
            "src/tutorials/elements/dataframes/dataframe-row-selections.py",
            title="Dataframe Row Selections",
        ),
        st.Page(
            "src/tutorials/elements/charts/annotations-in-altair.py",
            title="Annotations in Altair",
        ),
        st.Page(
            "src/tutorials/execution-flow/fragments/tutorial-fragment-rerun.py",
            title="Tutorial Fragment ReRun",
        ),
        st.Page(
            "src/tutorials/execution-flow/fragments/tutorial-fragment-streaming.py",
            title="Tutorial Fragment Streaming",
        ),
        st.Page(
            "src/tutorials/execution-flow/fragments/tutorial-fragment-multiple-container.py",
            title="Tutorial Fragment Multiple Container",
        ),
        st.Page("src/tutorials/create-a-simple-grid.py", title="Create a Simple Grid"),
    ],
    "Tutorials/dynamic-navigation": [
        st.Page("src/tutorials/dynamicnavigation/dynamic-navigation.py",title="Dynamic Navigation",),
        st.Page("src/tutorials/dynamicnavigation/admin/admin_1.py", title="Admin  1"),
        st.Page("src/tutorials/dynamicnavigation/admin/admin_2.py", title="Admin  2"),
        st.Page("src/tutorials/dynamicnavigation/respond/respond_2.py", title="Respond  2"),
        st.Page("src/tutorials/dynamicnavigation/respond/respond_1.py", title="Respond  1"),
        st.Page("src/tutorials/dynamicnavigation/settings.py", title="Settings"),
        st.Page(
            "src/tutorials/dynamicnavigation/request/request_1.py", title="Request  1"
        ),
        st.Page(
            "src/tutorials/dynamicnavigation/request/request_2.py", title="Request  2"
        ),
    ],
    "Tutorials/chat": [
        st.Page(
            "src/tutorials/chat/tutorial-chat-feedback.py",
            title="Tutorial-chat-feedback",
        ),
        st.Page(
            "src/tutorials/chat/tutorial-chat-revision.py",
            title="Tutorial-chat-revision",
        ),
    ],
    "Hello": [
        st.Page("src/hello/hello.py", title="Hello"),
    ],
    "Text": [
        st.Page("src/text/badge.py", title="Badge"),
        st.Page("src/text/caption.py", title="Caption"),
        st.Page("src/text/code-ascii.py", title="Code-ascii"),
        st.Page("src/text/code.py", title="Code"),
        st.Page("src/text/header.py", title="Header"),
        st.Page("src/text/latex.py", title="Latex"),
        st.Page("src/text/markdown.py", title="Markdown"),
        st.Page("src/text/markdown1.py", title="Markdown 1"),
        st.Page("src/text/subheader.py", title="Subheader"),
        st.Page("src/text/text_area.py", title="Text Area"),
        st.Page("src/text/text.py", title="Text"),
        st.Page("src/text/title.py", title="Title"),
        st.Page("src/text/write_stream.py", title="Write Stream"),
        st.Page("src/text/write1.py", title="Write 1"),
        st.Page("src/text/write2.py", title="Write 2"),
        st.Page("src/text/write3.py", title="Write 3"),
    ],
    "st-experimental-connection/util": [
        st.Page(
            "src/st-experimental-connection/util/release_helper.py",
            title="Release Helper",
        ),
    ],
    "st-experimental-connection/1.22/st-experimental-connection": [
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/🔌_Home.py",
            title="🔌 Home",
        ),
    ],
    "st-experimental-connection/1.22/st-experimental-connection/duckdb_connection": [
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/duckdb_connection/__init__.py",
            title="_ Init _",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/duckdb_connection/connection.py",
            title="Connection",
        ),
    ],
    "st-experimental-connection/1.22/st-experimental-connection/pages": [
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/05_🏂_Snowpark.py",
            title="05 🏂 Snowpark",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/01_🧰_Connection_setup.py",
            title="01 🧰 Connection Setup",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/07_🏗️_Build_your_own.py",
            title="07 🏗️ Build Your Own",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/04_🗂️_S3,_GCS,_and_cloud_files.py",
            title="04_🗂️_S3, GCS, And Cloud Files",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/03_🏰_SQL.py",
            title="03 🏰 SQL",
        ),
        st.Page(
            "src/st-experimental-connection/1.22/st-experimental-connection/pages/06_🙌_Community_connections.py",
            title="06 🙌 Community Connections",
        ),
    ],
    "Metric": [
        st.Page("src/metric/example1.py", title="Metric.example 1"),
        st.Page("src/metric/example5.py", title="Metric.example 5"),
        st.Page("src/metric/example4.py", title="Metric.example 4"),
        st.Page("src/metric/example3.py", title="Metric.example 3"),
        st.Page("src/metric/example2.py", title="Metric.example 2"),
    ],
    "Data": [
        st.Page("src/data/data_editor2.py", title="Data.data Editor 2"),
        st.Page("src/data/table.py", title="Data.table"),
        st.Page("src/data/json_column.py", title="Data.json Column"),
        st.Page("src/data/areachart_column.py", title="Data.areachart Column"),
        st.Page("src/data/column_config.py", title="Data.column Config"),
        st.Page("src/data/selectbox_column.py", title="Data.selectbox Column"),
        st.Page("src/data/dataframe2.py", title="Data.dataframe 2"),
        st.Page("src/data/json.py", title="Data.json"),
        st.Page("src/data/linechart_column.py", title="Data.linechart Column"),
        st.Page("src/data/column_config.empty.py", title="Data.column Config.empty"),
        st.Page("src/data/date_column.py", title="Data.date Column"),
        st.Page("src/data/text_column.py", title="Data.text Column"),
        st.Page("src/data/number_column.py", title="Data.number Column"),
        st.Page("src/data/data_editor3.py", title="Data.data Editor 3"),
        st.Page("src/data/barchart_column.py", title="Data.barchart Column"),
        st.Page("src/data/link_column.py", title="Data.link Column"),
        st.Page("src/data/table_markdown.py", title="Data.table Markdown"),
        st.Page("src/data/datetime_column.py", title="Data.datetime Column"),
        st.Page("src/data/time_column.py", title="Data.time Column"),
        st.Page(
            "src/data/dataframe_config_index.py", title="Data.dataframe Config Index"
        ),
        st.Page("src/data/column.py", title="Data.column"),
        st.Page(
            "src/data/dataframe_event_state_selections.py",
            title="Data.dataframe Event State Selections",
        ),
        st.Page("src/data/image_column.py", title="Data.image Column"),
        st.Page("src/data/dataframe.py", title="Data.dataframe"),
        st.Page("src/data/data_editor.py", title="Data.data Editor"),
        st.Page("src/data/dataframe_config.py", title="Data.dataframe Config"),
        st.Page("src/data/dataframe1.py", title="Data.dataframe 1"),
        st.Page("src/data/data_editor_config.py", title="Data.data Editor Config"),
        st.Page("src/data/list_column.py", title="Data.list Column"),
        st.Page("src/data/data_editor4.py", title="Data.data Editor 4"),
        st.Page("src/data/progress_column.py", title="Data.progress Column"),
        st.Page("src/data/data_editor1.py", title="Data.data Editor 1"),
        st.Page("src/data/checkbox_column.py", title="Data.checkbox Column"),
    ],
    "Media": [
        st.Page("src/media/logo.py", title="Logo"),
    ],
    "Functions": [
            page1,
            page2,
    ]
}


# -------------------------------------------------------------------------------------------------
if "top" not in st.session_state:
    st.session_state.top = False

top = "top" if st.session_state.top else "sidebar"


# -------------------------------------------------------------------------------------------------
st.sidebar.checkbox("Top Navigation", key="top")

st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

# -------------------------------------------------------------------------------------------------
pg = st.navigation(pages, position=top, expanded=False)
pg.run()
