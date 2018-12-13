#include "testlib.h"
#include <vector>

int const MAX_WEIGHT = 1000 * 1000 * 1000;

void GenSums(int idx, long long sum, std::vector<int> const &weights, std::vector<bool> &covered) {
    if (idx == (int)weights.size()) {
        if (sum >= 1LL && sum < (long long)covered.size()) {
            covered[sum] = true;
        }
        return;
    }
    
    GenSums(idx + 1, sum, weights, covered);
    GenSums(idx + 1, sum - (long long)weights[idx], weights, covered);
    GenSums(idx + 1, sum + (long long)weights[idx], weights, covered);
}

void CheckSolution(std::vector<int> const &part_weights, int n, int judge_answer) {
    int part_cnt = (int)part_weights.size();
    
    if (part_cnt > judge_answer) {
        quitf(_wa, "Found %d expected %d", part_cnt, judge_answer);
    }
    
    std::vector<bool> covered(n + 1, false);
    GenSums(0, 0, part_weights, covered);
    
    for (int i = 1; i != n; ++i) {
        if (!covered[i] && !covered[i + 1]) {
            quitf(_wa, "Weight %d is not covered", i);
        }
    }
    
    if (part_cnt < judge_answer) {
        quitf(_fail, "Found %d expected %d", part_cnt, judge_answer);
    } else {
        if (part_cnt == 1) {
            quitf(_ok, "1 weight");
        }
        quitf(_ok, "%d weights", part_cnt);
    }
}

std::vector<int> Read(InStream &stream) {
    std::vector<int> weights;
    while (!stream.seekEof()) {
        weights.push_back(stream.readInt(1, MAX_WEIGHT));
    }
    return weights;
}

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);
    
    int n = inf.readInt();
    
    std::vector<int> ja = Read(ans);
    std::vector<int> pa = Read(ouf);
    
    CheckSolution(pa, n, (int)ja.size());
}

