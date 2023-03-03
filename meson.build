project('iu9lab-web', 'cpp',  default_options : ['cpp_std=c++20', 'default_library=static'])

pistache_dep = dependency('pistache', fallback: ['pistache', 'pistache_dep'], default_options: ['default_library=static'])

src = [
  'src/swagger/api/DefaultApi.cpp',
  'src/swagger/impl/DefaultApiImpl.cpp',
'src/swagger/model/Error.cpp',
'src/swagger/model/Inline_response_200.cpp',
'src/swagger/model/ModelBase.cpp',
'src/swagger/model/ReportData.cpp',
  'src/main.cpp'
]

exe = executable('iu9lab-web', sources: src,
                         dependencies: [pistache_dep],
                         include_directories : include_directories(
                         'src/swagger/api',
                         'src/swagger/impl',
                         'src/swagger/model',
                         ))
