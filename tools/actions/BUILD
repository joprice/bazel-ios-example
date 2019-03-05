load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

py_proto_library(
    name = "extra_actions_base_pb2",
    srcs = ["extra_actions_base.proto"],
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
    #deps = [":build_pb_py"],
)

py_binary(
    name = "generate_compile_command",
    srcs = [
        "generate_compile_command.py",
    ],
    deps = ["extra_actions_base_pb2"],
)

extra_action(
    name = "generate_compile_commands_action",
    cmd = "$(location :generate_compile_command) $(EXTRA_ACTION_FILE)" +
          " $(output $(ACTION_ID)_compile_command)",
    out_templates = [
        "$(ACTION_ID)_compile_command",
    ],
    tools = [
        ":generate_compile_command",
    ],
)

action_listener(
    name = "generate_compile_commands_listener",
    extra_actions = [":generate_compile_commands_action"],
    mnemonics = [
        "ObjcCompile",
        #'CppCompile',
    ],
    visibility = ["//visibility:public"],
)
