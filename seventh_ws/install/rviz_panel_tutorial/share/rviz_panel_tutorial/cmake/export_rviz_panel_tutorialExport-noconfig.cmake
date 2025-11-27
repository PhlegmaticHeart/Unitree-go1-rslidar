#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rviz_panel_tutorial::demo_panel" for configuration ""
set_property(TARGET rviz_panel_tutorial::demo_panel APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(rviz_panel_tutorial::demo_panel PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libdemo_panel.so"
  IMPORTED_SONAME_NOCONFIG "libdemo_panel.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS rviz_panel_tutorial::demo_panel )
list(APPEND _IMPORT_CHECK_FILES_FOR_rviz_panel_tutorial::demo_panel "${_IMPORT_PREFIX}/lib/libdemo_panel.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
