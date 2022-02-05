import conbench.runner

from functions import benchmarkable_function


@conbench.runner.register_benchmark
class SimpleBenchmark(conbench.runner.Benchmark):
    name = "simple-benchmark"

    def run(self, **kwargs):
        yield self.conbench.benchmark(
            self._get_benchmark_function(), self.name, options=kwargs
        )

    def _get_benchmark_function(self):
        return lambda: benchmarkable_function()
