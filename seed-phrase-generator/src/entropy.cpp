#include "entropy.hpp"
#include <random>
#include <stdexcept>

namespace seed {

std::vector<uint8_t> generate_entropy(size_t bytes) {
    if (bytes == 0) throw std::invalid_argument("Entropy bytes must be > 0");
    if (bytes % 4 != 0) throw std::invalid_argument("Entropy bytes must be multiple of 4");

    std::vector<uint8_t> entropy(bytes);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, 255);

    for (auto& byte : entropy) {
        byte = static_cast<uint8_t>(dist(gen));
    }
    return entropy;
}

} // namespace seed