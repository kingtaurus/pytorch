from torch.testing._internal.common_utils import run_tests

import torch
import unittest

class TestPublicBindings(unittest.TestCase):
    def test_no_new_bindings(self):
        """
        This test aims to stop the introduction of new JIT bindings into torch._C
        whose names do not start with _. Such bindings are made available as
        torch.XXX, which may not be desirable.

        If your change causes this test to fail, add your new binding to a relevant
        submodule of torch._C, such as torch._C._jit (or other relevant submodule of
        torch._C). If your binding really needs to be available as torch.XXX, add it
        to torch._C and add it to the allowlist below.

        If you have removed a binding, remove it from the allowlist as well.
        """
        # This allowlist contains every binding in torch._C that is copied into torch at
        # the time of writing. It was generated with
        #
        #   {elem for elem in dir(torch._C) if not elem.startswith("_")}
        #
        torch_C_allowlist = {
            "AVG",
            "AggregationType",
            "AnyType",
            "Argument",
            "ArgumentSpec",
            "BFloat16StorageBase",
            "BenchmarkConfig",
            "BenchmarkExecutionStats",
            "Block",
            "BoolStorageBase",
            "BoolType",
            "BufferDict",
            "ByteStorageBase",
            "CONV_BN_FUSION",
            "CallStack",
            "Capsule",
            "CharStorageBase",
            "ClassType",
            "Code",
            "CompilationUnit",
            "CompleteArgumentSpec",
            "ComplexDoubleStorageBase",
            "ComplexFloatStorageBase",
            "ComplexType",
            "ConcreteModuleType",
            "ConcreteModuleTypeBuilder",
            "CudaBFloat16StorageBase",
            "CudaBFloat16TensorBase",
            "CudaBoolStorageBase",
            "CudaBoolTensorBase",
            "CudaByteStorageBase",
            "CudaByteTensorBase",
            "CudaCharStorageBase",
            "CudaCharTensorBase",
            "CudaComplexDoubleStorageBase",
            "CudaComplexDoubleTensorBase",
            "CudaComplexFloatStorageBase",
            "CudaComplexFloatTensorBase",
            "CudaDoubleStorageBase",
            "CudaDoubleTensorBase",
            "CudaFloatStorageBase",
            "CudaFloatTensorBase",
            "CudaHalfStorageBase",
            "CudaHalfTensorBase",
            "CudaIntStorageBase",
            "CudaIntTensorBase",
            "CudaLongStorageBase",
            "CudaLongTensorBase",
            "CudaShortStorageBase",
            "CudaShortTensorBase",
            "DeepCopyMemoTable",
            "DeviceObjType",
            "DictType",
            "DisableTorchFunction",
            "DoubleStorageBase",
            "EnumType",
            "ErrorReport",
            "ExecutionPlan",
            "FUSE_ADD_RELU",
            "FatalError",
            "FileCheck",
            "FloatStorageBase",
            "FloatType",
            "FunctionSchema",
            "Future",
            "FutureType",
            "Generator",
            "Gradient",
            "Graph",
            "GraphExecutorState",
            "HOIST_CONV_PACKED_PARAMS",
            "HalfStorageBase",
            "INSERT_FOLD_PREPACK_OPS",
            "IODescriptor",
            "InferredType",
            "IntStorageBase",
            "IntType",
            "InterfaceType",
            "JITException",
            "ListType",
            "LiteScriptModule",
            "LockingLogger",
            "LoggerBase",
            "LongStorageBase",
            "MobileOptimizerType",
            "ModuleDict",
            "Node",
            "NoneType",
            "NoopLogger",
            "NumberType",
            "OptionalType",
            "ParameterDict",
            "PyObjectType",
            "PyTorchFileReader",
            "PyTorchFileWriter",
            "QInt32StorageBase",
            "QInt8StorageBase",
            "QUInt4x2StorageBase",
            "QUInt8StorageBase",
            "REMOVE_DROPOUT",
            "RRefType",
            "SUM",
            "ScriptClass",
            "ScriptClassFunction",
            "ScriptFunction",
            "ScriptMethod",
            "ScriptModule",
            "ScriptObject",
            "ShortStorageBase",
            "Size",
            "StaticRuntime",
            "Stream",
            "StreamObjType",
            "StringType",
            "TensorType",
            "ThroughputBenchmark",
            "TracingState",
            "TupleType",
            "Type",
            "Use",
            "Value",
            "autocast_decrement_nesting",
            "autocast_increment_nesting",
            "clear_autocast_cache",
            "cpp",
            "default_generator",
            "device",
            "dtype",
            "finfo",
            "fork",
            "get_default_dtype",
            "get_num_interop_threads",
            "get_num_threads",
            "has_cuda",
            "has_cudnn",
            "has_lapack",
            "has_mkl",
            "has_mkldnn",
            "has_mlc",
            "has_openmp",
            "iinfo",
            "import_ir_module",
            "import_ir_module_from_buffer",
            "init_num_threads",
            "is_anomaly_enabled",
            "is_autocast_enabled",
            "is_grad_enabled",
            "layout",
            "memory_format",
            "merge_type_from_type_comment",
            "parse_ir",
            "parse_schema",
            "parse_type_comment",
            "qscheme",
            "set_anomaly_enabled",
            "set_autocast_enabled",
            "set_flush_denormal",
            "set_num_interop_threads",
            "set_num_threads",
            "unify_type_list",
            "wait",
        }
        torch_C_bindings = {elem for elem in dir(torch._C) if not elem.startswith("_")}

        # Check that both sets above have the same elements as each other.
        self.assertSetEqual(torch_C_bindings.symmetric_difference(torch_C_bindings), set())


if __name__ == '__main__':
    run_tests()
