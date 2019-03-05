# see https://stackoverflow.com/questions/46619281/why-is-a-publicly-visible-bazel-protobuf-target-not-declared
# Note, the suggested fix did not work, but the OP workaround does
genrule(
    name = "copy_six",
    srcs = ["six-1.10.0/six.py"],
    outs = ["six.py"],
    cmd = "cp $< $(@)",
)

py_library(
    name = "six",
    srcs = ["six.py"],
    srcs_version = "PY2AND3",
    visibility = ["//visibility:public"],
)
