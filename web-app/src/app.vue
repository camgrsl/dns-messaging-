<template>
<section class="antialiased bg-gray-100 text-gray-600 h-screen px-4">
    <div class="flex flex-col justify-center h-full">
        <!-- Table -->
        <div class="w-full max-w-2xl mx-auto bg-white shadow-lg rounded-sm border border-gray-200">
            <header class="px-5 py-4 border-b border-gray-100">
                <h2 class="font-semibold text-gray-800">Gouach Battery Monitoring</h2>
            </header>
            <div class="p-3">
                <div class="overflow-x-auto">
                    <table class="table-auto w-full">
                        <thead class="text-xs font-semibold uppercase text-gray-400 bg-gray-50">
                            <tr>
                                <th class="p-2 whitespace-nowrap">
                                    <div class="font-semibold text-left">Battery ID</div>
                                </th>
                                <th class="p-2 whitespace-nowrap">
                                    <div class="font-semibold text-left">Battery level</div>
                                </th>
                                <th class="p-2 whitespace-nowrap">
                                    <div class="font-semibold text-left">Reported on</div>
                                </th>
                            </tr>
                        </thead>
                        <tbody class="text-sm divide-y divide-gray-100">
                            <tr v-for="(meta, id) in batteries">
                                <td class="p-2 whitespace-nowrap">
                                    <div class="flex items-center">
                                        <div class="font-medium text-gray-800">{{ id }}</div>
                                    </div>
                                </td>
     
                                <td class="p-2 whitespace-nowrap">
                                    <div 
                                      class="text-left font-medium"
                                      :class="{
                                        'text-green-500': meta.level >= 50,
                                        'text-red-500': meta.level <= 20,
                                        'text-orange-500': meta.level > 20 && meta.level < 50
                                      }"
                                    >{{ meta.level }}%</div>
                                </td>
                                <td class="p-2 whitespace-nowrap">
                                    <div class="text-left">Nov 25 2022 at 2:23pm</div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</section>
</template>

<script setup>
  const { data: batteries } = await useFetch('http://api:3000')
</script>
